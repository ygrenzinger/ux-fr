#!/usr/bin/env python3
"""Idempotent WordPress to Hugo migration for ux-fr.com."""

from __future__ import annotations

import argparse
import email.utils
import hashlib
import html
import json
import mimetypes
import os
import posixpath
import re
import shutil
import sys
import time
from dataclasses import dataclass
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qsl, quote, unquote, urljoin, urlparse, urlunparse
from urllib.request import Request, urlopen


SITE_URL = "https://ux-fr.com"
API_URL = f"{SITE_URL}/wp-json/wp/v2"
ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIR = ROOT / "content"
STATIC_DIR = ROOT / "static"
PLACEHOLDER_PATH = "/images/placeholder.svg"
REPORT_PATH = ROOT / "migration-report.json"
USER_AGENT = "ux-fr-hugo-migration/1.0 (+https://ux-fr.com/)"
DOWNLOAD_EXTENSIONS = {
    ".pdf",
    ".doc",
    ".docx",
    ".xls",
    ".xlsx",
    ".ppt",
    ".pptx",
    ".zip",
    ".mp3",
    ".mp4",
    ".mov",
    ".webm",
}


def request_json(url: str) -> tuple[Any, dict[str, str]]:
    body, headers = request_bytes(url, accept="application/json")
    return json.loads(body.decode("utf-8")), headers


def request_bytes(
    url: str,
    accept: str = "*/*",
    retries: int = 2,
    timeout: int = 30,
) -> tuple[bytes, dict[str, str]]:
    req = Request(url, headers={"User-Agent": USER_AGENT, "Accept": accept})
    last_error: Exception | None = None
    for attempt in range(retries + 1):
        try:
            with urlopen(req, timeout=timeout) as response:
                headers = {k.lower(): v for k, v in response.headers.items()}
                return response.read(), headers
        except (HTTPError, URLError, TimeoutError) as exc:
            last_error = exc
            if attempt < retries:
                time.sleep(1 + attempt)
    raise RuntimeError(f"Failed to fetch {url}: {last_error}")


def fetch_collection(endpoint: str, params: dict[str, str] | None = None) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    page = 1
    while True:
        query = {"per_page": "100", "page": str(page)}
        if params:
            query.update(params)
        qs = "&".join(f"{quote(k)}={quote(v)}" for k, v in query.items())
        url = f"{API_URL}/{endpoint}?{qs}"
        try:
            data, headers = request_json(url)
        except RuntimeError as exc:
            if "400" in str(exc) and page > 1:
                break
            raise
        if not isinstance(data, list):
            raise RuntimeError(f"Unexpected response for {endpoint}: {type(data)}")
        items.extend(data)
        total_pages = int(headers.get("x-wp-totalpages", "1") or "1")
        if page >= total_pages or not data:
            break
        page += 1
    return items


def strip_tags(value: str) -> str:
    return normalize_text(re.sub(r"<[^>]+>", "", html.unescape(value or "")))


def normalize_text(value: str) -> str:
    value = html.unescape(value or "")
    value = value.replace("\xa0", " ")
    value = value.replace("\u2009", " ")
    value = value.replace("\r\n", "\n").replace("\r", "\n")
    value = re.sub(r"[ \t]+", " ", value)
    value = re.sub(r"\n{3,}", "\n\n", value)
    return value.strip()


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def yaml_list(values: list[str]) -> str:
    return "[" + ", ".join(yaml_string(v) for v in values) + "]"


def iso_datetime(value: str) -> str:
    if not value:
        return ""
    return value if value.endswith(("Z", "+00:00")) else value


def original_path(link: str) -> str:
    parsed = urlparse(link)
    path = parsed.path or "/"
    if not path.endswith("/"):
        path += "/"
    return path


def content_filename(item: dict[str, Any], kind: str) -> Path:
    slug = item.get("slug") or str(item["id"])
    if kind == "post":
        date = item.get("date", "")[:10] or "undated"
        return CONTENT_DIR / "posts" / f"{date}-{slug}.md"
    return CONTENT_DIR / f"{slug}.md"


def clean_shortcode_text(markdown: str) -> str:
    markdown = re.sub(r"\[easy_contact_forms[^\]]*\]", "", markdown, flags=re.I)
    markdown = re.sub(r"\[contact-form[^\]]*\].*?\[/contact-form\]", "", markdown, flags=re.I | re.S)
    markdown = re.sub(r"(?m)^\s*\[[A-Za-z0-9_-]+(?:\s+[^\]]*)?\]\s*$", "", markdown)
    return re.sub(r"\n{3,}", "\n\n", markdown).strip() + "\n"


def slugish(value: str) -> str:
    value = unquote(value)
    value = re.sub(r"[^A-Za-z0-9_.-]+", "-", value).strip("-")
    return value or "asset"


def local_asset_path(url: str) -> Path:
    parsed = urlparse(url)
    path = unquote(parsed.path)
    if "/wp-content/uploads/" in path:
        relative = path.split("/wp-content/uploads/", 1)[1]
        return STATIC_DIR / "wp-content" / "uploads" / relative.lstrip("/")
    suffix = Path(path).suffix
    if not suffix:
        suffix = mimetypes.guess_extension(mimetypes.guess_type(path)[0] or "") or ".bin"
    digest = hashlib.sha1(url.encode("utf-8")).hexdigest()[:12]
    name = f"{slugish(Path(path).stem)}-{digest}{suffix}"
    return STATIC_DIR / "migrated-media" / name


def public_path_for_static(path: Path) -> str:
    return "/" + path.relative_to(STATIC_DIR).as_posix()


@dataclass
class MigrationState:
    downloaded_assets: dict[str, str]
    failed_assets: dict[str, str]
    internal_urls: set[str]
    generated_urls: list[str]
    removed_shortcodes: int = 0


class MarkdownConverter(HTMLParser):
    def __init__(self, state: MigrationState):
        super().__init__(convert_charrefs=True)
        self.state = state
        self.parts: list[str] = []
        self.link_stack: list[dict[str, str]] = []
        self.list_stack: list[str] = []
        self.skip_depth = 0
        self.pre_depth = 0

    def convert(self, value: str) -> str:
        value = re.sub(r"<!--.*?-->", "", value or "", flags=re.S)
        self.feed(value)
        self.close()
        markdown = "".join(self.parts)
        markdown = normalize_markdown(markdown)
        before = markdown
        markdown = clean_shortcode_text(markdown)
        self.state.removed_shortcodes += before.count("[easy_contact_forms")
        return markdown

    def handle_starttag(self, tag: str, attrs_list: list[tuple[str, str | None]]) -> None:
        attrs = {k.lower(): v or "" for k, v in attrs_list}
        tag = tag.lower()
        classes = attrs.get("class", "")
        if tag in {"script", "style", "noscript", "form"} or "comment" in classes:
            self.skip_depth += 1
            return
        if self.skip_depth:
            return
        if tag in {"p", "div", "section", "article"}:
            self.ensure_block()
        elif tag in {"br"}:
            self.emit("  \n")
        elif tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.ensure_block()
            self.emit("#" * int(tag[1]) + " ")
        elif tag == "blockquote":
            self.ensure_block()
            self.emit("> ")
        elif tag in {"strong", "b"}:
            self.emit("**")
        elif tag in {"em", "i"}:
            self.emit("*")
        elif tag == "code":
            self.emit("`")
        elif tag == "pre":
            self.pre_depth += 1
            self.ensure_block()
            self.emit("```\n")
        elif tag == "a":
            self.link_stack.append({"href": self.normalize_href(attrs.get("href", "")), "text": ""})
        elif tag == "img":
            self.handle_image(attrs)
        elif tag in {"ul", "ol"}:
            self.list_stack.append(tag)
            self.ensure_block()
        elif tag == "li":
            self.ensure_line()
            bullet = "1. " if self.list_stack and self.list_stack[-1] == "ol" else "- "
            self.emit(bullet)
        elif tag in {"table", "iframe"}:
            self.ensure_block()
            self.emit(self.get_starttag_text() or "")

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if self.skip_depth:
            self.skip_depth -= 1
            return
        if tag in {"p", "div", "section", "article", "blockquote"}:
            self.ensure_block()
        elif tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.ensure_block()
        elif tag in {"strong", "b"}:
            self.emit("**")
        elif tag in {"em", "i"}:
            self.emit("*")
        elif tag == "code":
            self.emit("`")
        elif tag == "pre":
            self.emit("\n```\n\n")
            self.pre_depth = max(0, self.pre_depth - 1)
        elif tag == "a":
            link = self.link_stack.pop() if self.link_stack else {"href": "", "text": ""}
            href = link.get("href", "")
            text = normalize_markdown(link.get("text", "")).strip()
            if href and text:
                self.emit(f"[{text}]({href})")
            elif href:
                self.emit(f"<{href}>")
            else:
                self.emit(text)
        elif tag in {"ul", "ol"}:
            if self.list_stack:
                self.list_stack.pop()
            self.ensure_block()
        elif tag == "li":
            self.emit("\n")
        elif tag in {"table", "iframe"}:
            self.emit(f"</{tag}>")
            self.ensure_block()

    def handle_data(self, data: str) -> None:
        if self.skip_depth:
            return
        if self.pre_depth:
            self.emit(data)
        else:
            self.emit(normalize_inline(data))

    def handle_entityref(self, name: str) -> None:
        self.handle_data(html.unescape(f"&{name};"))

    def handle_charref(self, name: str) -> None:
        self.handle_data(html.unescape(f"&#{name};"))

    def emit(self, value: str) -> None:
        if not value:
            return
        if self.link_stack:
            self.link_stack[-1]["text"] += value
        else:
            self.parts.append(value)

    def ensure_block(self) -> None:
        text = "".join(self.parts)
        if text and not text.endswith("\n\n"):
            self.parts.append("\n\n" if text.endswith("\n") else "\n\n")

    def ensure_line(self) -> None:
        text = "".join(self.parts)
        if text and not text.endswith("\n"):
            self.parts.append("\n")

    def normalize_href(self, href: str) -> str:
        if not href or href.startswith("#") or href.startswith(("mailto:", "tel:")):
            return href
        absolute = urljoin(SITE_URL, href)
        parsed = urlparse(absolute)
        path = parsed.path or "/"
        if parsed.netloc in {"ux-fr.com", "www.ux-fr.com"}:
            if "/comment-page-" in path or parsed.fragment.startswith("comment-"):
                return path.split("/comment-page-", 1)[0] or "/"
            query = ""
            keep = [(k, v) for k, v in parse_qsl(parsed.query) if not k.startswith("utm_")]
            if keep:
                query = "&".join(f"{quote(k)}={quote(v)}" for k, v in keep)
            return urlunparse(("", "", path, "", query, ""))
        suffix = Path(path).suffix.lower()
        if suffix in DOWNLOAD_EXTENSIONS:
            return download_asset(absolute, self.state)
        return absolute

    def handle_image(self, attrs: dict[str, str]) -> None:
        src = attrs.get("src", "")
        if not src:
            return
        alt = normalize_text(attrs.get("alt", "") or attrs.get("title", ""))
        public = download_asset(urljoin(SITE_URL, src), self.state)
        title = normalize_text(attrs.get("title", ""))
        title_part = f' "{title}"' if title else ""
        self.emit(f"![{alt}]({public}{title_part})")


def normalize_inline(value: str) -> str:
    value = html.unescape(value).replace("\xa0", " ")
    value = re.sub(r"[ \t\n\r]+", " ", value)
    return value


def normalize_markdown(value: str) -> str:
    lines = [line.rstrip() for line in value.splitlines()]
    value = "\n".join(lines)
    value = re.sub(r" +\n", "\n", value)
    value = re.sub(r"\n{3,}", "\n\n", value)
    return value.strip()


def download_asset(url: str, state: MigrationState) -> str:
    if not url or url.startswith("data:"):
        return PLACEHOLDER_PATH
    if url in state.downloaded_assets:
        return state.downloaded_assets[url]
    if url in state.failed_assets:
        return PLACEHOLDER_PATH
    target = local_asset_path(url)
    public = public_path_for_static(target)
    if target.exists() and target.stat().st_size > 0:
        state.downloaded_assets[url] = public
        return public
    target.parent.mkdir(parents=True, exist_ok=True)
    try:
        body, headers = request_bytes(url, retries=0, timeout=8)
        if not body or len(body) < 64:
            raise RuntimeError("empty or tiny asset")
        content_type = headers.get("content-type", "")
        if "text/html" in content_type and Path(target).suffix.lower() not in {".html", ".htm"}:
            raise RuntimeError(f"unexpected HTML response for asset ({content_type})")
        tmp = target.with_suffix(target.suffix + ".tmp")
        tmp.write_bytes(body)
        tmp.replace(target)
        state.downloaded_assets[url] = public
        return public
    except Exception as exc:
        state.failed_assets[url] = str(exc)
        return PLACEHOLDER_PATH


def term_names(item: dict[str, Any], taxonomy: str, terms: dict[int, dict[str, Any]]) -> list[str]:
    return [terms[i]["name"] for i in item.get(taxonomy, []) if i in terms]


def author_name(item: dict[str, Any], authors: dict[int, dict[str, Any]]) -> str:
    author_id = item.get("author")
    return authors.get(author_id, {}).get("name", "UX-FR")


def write_content(
    item: dict[str, Any],
    kind: str,
    state: MigrationState,
    authors: dict[int, dict[str, Any]],
    categories: dict[int, dict[str, Any]],
    tags: dict[int, dict[str, Any]],
) -> None:
    title = strip_tags(item.get("title", {}).get("rendered", ""))
    raw_content = item.get("content", {}).get("rendered", "")
    converter = MarkdownConverter(state)
    body = converter.convert(raw_content)
    summary = strip_tags(item.get("excerpt", {}).get("rendered", ""))
    link = item.get("link") or item.get("guid", {}).get("rendered", "")
    url_path = original_path(link)
    state.generated_urls.append(url_path)
    state.internal_urls.add(url_path)
    aliases = legacy_aliases(url_path)
    front = {
        "title": title,
        "date": iso_datetime(item.get("date", "")),
        "lastmod": iso_datetime(item.get("modified", "")),
        "url": url_path,
        "summary": summary,
        "author": author_name(item, authors),
        "canonicalURL": f"https://ux-fr.com{url_path}",
        "draft": False,
    }
    if kind == "post":
        front["categories"] = term_names(item, "categories", categories)
        front["tags"] = term_names(item, "tags", tags)
    if aliases:
        front["aliases"] = aliases
    featured = item.get("featured_media")
    if featured:
        media_url = item.get("_embedded", {}).get("wp:featuredmedia", [{}])[0].get("source_url")
        if media_url:
            front["cover"] = {"image": download_asset(media_url, state), "relative": False}
    target = content_filename(item, kind)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(render_front_matter(front) + "\n" + body, encoding="utf-8")


def legacy_aliases(path: str) -> list[str]:
    aliases: list[str] = []
    if path.startswith("/20"):
        aliases.append(path.rstrip("/"))
    return aliases


def render_front_matter(data: dict[str, Any]) -> str:
    lines = ["---"]
    for key, value in data.items():
        if value in (None, "", [], {}):
            continue
        if isinstance(value, bool):
            lines.append(f"{key}: {'true' if value else 'false'}")
        elif isinstance(value, list):
            lines.append(f"{key}: {yaml_list([str(v) for v in value])}")
        elif isinstance(value, dict):
            lines.append(f"{key}:")
            for subkey, subvalue in value.items():
                if isinstance(subvalue, bool):
                    lines.append(f"  {subkey}: {'true' if subvalue else 'false'}")
                else:
                    lines.append(f"  {subkey}: {yaml_string(str(subvalue))}")
        else:
            lines.append(f"{key}: {yaml_string(str(value))}")
    lines.append("---")
    return "\n".join(lines)


def write_taxonomy_metadata(terms: dict[int, dict[str, Any]], kind: str) -> None:
    for term in terms.values():
        slug = term.get("slug")
        if not slug:
            continue
        path = CONTENT_DIR / kind / slug / "_index.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        data = {
            "title": strip_tags(term.get("name", "")),
            "slug": slug,
            "url": original_path(term.get("link", f"https://ux-fr.com/{kind}/{slug}/")),
        }
        path.write_text(render_front_matter(data) + "\n", encoding="utf-8")


def write_author_metadata(authors: dict[int, dict[str, Any]]) -> None:
    for author in authors.values():
        slug = author.get("slug")
        if not slug:
            continue
        path = CONTENT_DIR / "author" / slug / "_index.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        body = normalize_text(author.get("description", ""))
        data = {
            "title": author.get("name", slug),
            "slug": slug,
            "url": original_path(author.get("link", f"https://ux-fr.com/author/{slug}/")),
        }
        path.write_text(render_front_matter(data) + "\n" + body + "\n", encoding="utf-8")


def clean_generated_content() -> None:
    for path in [CONTENT_DIR / "posts", CONTENT_DIR / "category", CONTENT_DIR / "tag", CONTENT_DIR / "author"]:
        if path.exists():
            shutil.rmtree(path)
    for md in CONTENT_DIR.glob("*.md"):
        if md.name not in {"archives.md", "search.md"}:
            md.unlink()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--clean", action="store_true", help="Remove previously generated migrated content first.")
    args = parser.parse_args()

    if args.clean:
        clean_generated_content()

    state = MigrationState(downloaded_assets={}, failed_assets={}, internal_urls=set(), generated_urls=[])
    posts = fetch_collection("posts", {"_embed": "1"})
    pages = fetch_collection("pages", {"_embed": "1"})
    authors_list = fetch_collection("users")
    categories_list = fetch_collection("categories")
    tags_list = fetch_collection("tags")

    authors = {item["id"]: item for item in authors_list}
    categories = {item["id"]: item for item in categories_list}
    tags = {item["id"]: item for item in tags_list}

    clean_generated_content()
    print(f"Fetched {len(posts)} posts, {len(pages)} pages, {len(categories)} categories, {len(tags)} tags.")
    for index, item in enumerate(posts, start=1):
        print(f"[posts {index}/{len(posts)}] {item.get('slug')}")
        write_content(item, "post", state, authors, categories, tags)
    for index, item in enumerate(pages, start=1):
        print(f"[pages {index}/{len(pages)}] {item.get('slug')}")
        write_content(item, "page", state, authors, categories, tags)
    write_taxonomy_metadata(categories, "category")
    write_taxonomy_metadata(tags, "tag")
    write_author_metadata(authors)

    report = {
        "generated_at": email.utils.format_datetime(datetime.now().astimezone()),
        "source": SITE_URL,
        "counts": {
            "posts": len(posts),
            "pages": len(pages),
            "authors": len(authors),
            "categories": len(categories),
            "tags": len(tags),
            "downloaded_assets": len(state.downloaded_assets),
            "failed_assets": len(state.failed_assets),
        },
        "generated_urls": sorted(set(state.generated_urls)),
        "failed_assets": state.failed_assets,
        "placeholder": PLACEHOLDER_PATH,
    }
    REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report["counts"], ensure_ascii=False, indent=2))
    if state.failed_assets:
        print(f"{len(state.failed_assets)} assets use the shared placeholder. See {REPORT_PATH.name}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
