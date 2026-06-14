#!/usr/bin/env python3
"""Audit linked images between ux-fr.com and the migrated Hugo site."""

from __future__ import annotations

import argparse
import json
import socket
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import asdict, dataclass
from html.parser import HTMLParser
from pathlib import Path


ORIGINAL_SITEMAP = "https://ux-fr.com/sitemap.xml"
NEW_SITEMAP = "https://ygrenzinger.github.io/ux-fr/sitemap.xml"
ORIGINAL_HOST = "ux-fr.com"
NEW_PREFIX = "https://ygrenzinger.github.io/ux-fr"


@dataclass
class LinkedImage:
    page_url: str
    page_path: str
    href: str
    href_status: int | None
    href_final_url: str | None
    href_error: str | None
    img_src: str
    img_path: str
    img_alt: str
    img_title: str
    local_static_path: str | None
    local_exists: bool


@dataclass
class CurrentLinkedImage:
    page_file: str
    page_path: str
    href: str
    href_status: int | None
    href_final_url: str | None
    href_error: str | None
    img_src: str
    img_exists: bool
    img_alt: str


class LinkedImageParser(HTMLParser):
    def __init__(self, page_url: str) -> None:
        super().__init__(convert_charrefs=True)
        self.page_url = page_url
        self.anchors: list[dict[str, str]] = []
        self.images: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {k.lower(): v or "" for k, v in attrs}
        if tag.lower() == "a":
            self.anchors.append(attrs_dict)
        elif tag.lower() == "img" and self.anchors:
            anchor = self.anchors[-1]
            href = urllib.parse.urljoin(self.page_url, anchor.get("href", ""))
            src = urllib.parse.urljoin(self.page_url, attrs_dict.get("src", ""))
            self.images.append(
                {
                    "href": href,
                    "img_src": src,
                    "img_alt": attrs_dict.get("alt", ""),
                    "img_title": attrs_dict.get("title", ""),
                }
            )

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "a" and self.anchors:
            self.anchors.pop()


def fetch(url: str, timeout: int = 20) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "ux-fr-link-audit/1.0"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read()


def get_sitemap_urls(sitemap_url: str) -> list[str]:
    body = fetch(sitemap_url)
    root = ET.fromstring(body)
    urls: list[str] = []
    for loc in root.findall(".//{*}loc"):
        if loc.text:
            value = loc.text.strip()
            if value.endswith(".xml"):
                urls.extend(get_sitemap_urls(value))
            else:
                urls.append(value)
    return sorted(dict.fromkeys(urls))


def check_url(url: str, timeout: int = 15) -> tuple[int | None, str | None, str | None]:
    if not url or url.startswith(("mailto:", "tel:", "javascript:", "#")):
        return None, None, "skipped scheme"

    headers = {"User-Agent": "ux-fr-link-audit/1.0"}
    for method in ("HEAD", "GET"):
        try:
            request = urllib.request.Request(url, headers=headers, method=method)
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return response.status, response.geturl(), None
        except urllib.error.HTTPError as exc:
            if method == "HEAD" and exc.code in {403, 405, 500, 501}:
                continue
            return exc.code, exc.geturl(), str(exc)
        except (urllib.error.URLError, socket.timeout, TimeoutError) as exc:
            if method == "HEAD":
                continue
            return None, None, str(exc)
    return None, None, "unknown error"


def original_path(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    return parsed.path or "/"


def local_static_path_for_image(root: Path, img_src: str) -> tuple[str, bool]:
    parsed = urllib.parse.urlparse(img_src)
    if parsed.netloc and parsed.netloc != ORIGINAL_HOST:
        return "", False
    if not parsed.path.startswith("/wp-content/"):
        return "", False
    local_path = root / "static" / parsed.path.lstrip("/")
    return str(local_path.relative_to(root)), local_path.exists()


def public_path_exists(root: Path, url: str) -> bool:
    parsed = urllib.parse.urlparse(url)
    path = parsed.path
    if path.startswith("/ux-fr/"):
        path = path.removeprefix("/ux-fr")
    elif path == "/ux-fr":
        path = "/"
    else:
        return False

    candidate = root / "public" / path.lstrip("/")
    if candidate.is_file():
        return True
    if candidate.is_dir() and (candidate / "index.html").is_file():
        return True
    if path.endswith("/"):
        return (candidate / "index.html").is_file()
    return False


def check_current_href(root: Path, href: str) -> tuple[int | None, str | None, str | None]:
    parsed = urllib.parse.urlparse(href)
    if not parsed.scheme and href.startswith("/"):
        return (200, href, None) if public_path_exists(root, href) else (404, href, "local file missing")
    if parsed.netloc == "ygrenzinger.github.io" and parsed.path.startswith("/ux-fr"):
        return (200, href, None) if public_path_exists(root, href) else (404, href, "local file missing")
    return check_url(href)


def audit_public(root: Path) -> tuple[list[CurrentLinkedImage], list[CurrentLinkedImage], list[CurrentLinkedImage]]:
    records: list[CurrentLinkedImage] = []
    status_cache: dict[str, tuple[int | None, str | None, str | None]] = {}
    for html_file in sorted((root / "public").rglob("*.html")):
        rel = html_file.relative_to(root / "public")
        if rel.name == "404.html":
            page_path = "/404.html"
        elif rel.name == "index.html":
            page_path = "/" + str(rel.parent).strip("/")
            if page_path != "/":
                page_path += "/"
        else:
            page_path = "/" + str(rel)
        page_url = urllib.parse.urljoin(NEW_PREFIX + "/", page_path.lstrip("/"))
        parser = LinkedImageParser(page_url)
        parser.feed(html_file.read_text(encoding="utf-8", errors="replace"))
        for image in parser.images:
            href = image["href"]
            if href not in status_cache:
                status_cache[href] = check_current_href(root, href)
                time.sleep(0.03)
            href_status, href_final_url, href_error = status_cache[href]
            img_src = image["img_src"]
            img_exists = public_path_exists(root, img_src)
            records.append(
                CurrentLinkedImage(
                    page_file=str(html_file.relative_to(root)),
                    page_path=page_path,
                    href=href,
                    href_status=href_status,
                    href_final_url=href_final_url,
                    href_error=href_error,
                    img_src=img_src,
                    img_exists=img_exists,
                    img_alt=image["img_alt"],
                )
            )
    broken_links = [
        record
        for record in records
        if record.href_status is None or record.href_status >= 400
    ]
    broken_images = [record for record in records if not record.img_exists]
    return records, broken_links, broken_images


def audit(root: Path) -> dict[str, object]:
    original_urls = get_sitemap_urls(ORIGINAL_SITEMAP)
    new_urls = get_sitemap_urls(NEW_SITEMAP)
    new_paths = {
        urllib.parse.urlparse(url).path.removeprefix("/ux-fr") or "/"
        for url in new_urls
    }

    records: list[LinkedImage] = []
    missing_new_pages: list[str] = []

    status_cache: dict[str, tuple[int | None, str | None, str | None]] = {}
    for index, page_url in enumerate(original_urls, start=1):
        page_path = original_path(page_url)
        if page_path not in new_paths:
            missing_new_pages.append(page_path)
        try:
            html = fetch(page_url).decode("utf-8", errors="replace")
        except Exception as exc:  # noqa: BLE001 - report and continue the audit.
            print(f"warn: cannot fetch {page_url}: {exc}", file=sys.stderr)
            continue

        parser = LinkedImageParser(page_url)
        parser.feed(html)
        for image in parser.images:
            href = image["href"]
            if href not in status_cache:
                status_cache[href] = check_url(href)
                time.sleep(0.05)
            href_status, href_final_url, href_error = status_cache[href]
            local_path, exists = local_static_path_for_image(root, image["img_src"])
            records.append(
                LinkedImage(
                    page_url=page_url,
                    page_path=page_path,
                    href=href,
                    href_status=href_status,
                    href_final_url=href_final_url,
                    href_error=href_error,
                    img_src=image["img_src"],
                    img_path=urllib.parse.urlparse(image["img_src"]).path,
                    img_alt=image["img_alt"],
                    img_title=image["img_title"],
                    local_static_path=local_path or None,
                    local_exists=exists,
                )
            )
        if index % 25 == 0:
            print(f"audited {index}/{len(original_urls)} pages", file=sys.stderr)

    broken = [
        record
        for record in records
        if record.href_status is None or record.href_status >= 400
    ]
    missing_local = [
        record
        for record in records
        if record.local_static_path and not record.local_exists
    ]
    current_records, current_broken_links, current_broken_images = audit_public(root)

    return {
        "original_sitemap": ORIGINAL_SITEMAP,
        "new_sitemap": NEW_SITEMAP,
        "original_pages": len(original_urls),
        "new_pages": len(new_urls),
        "missing_new_pages": missing_new_pages,
        "linked_images": [asdict(record) for record in records],
        "broken_linked_images": [asdict(record) for record in broken],
        "missing_local_images": [asdict(record) for record in missing_local],
        "current_linked_images": [asdict(record) for record in current_records],
        "current_broken_linked_images": [asdict(record) for record in current_broken_links],
        "current_broken_image_sources": [asdict(record) for record in current_broken_images],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="docs/linked-image-audit.json")
    args = parser.parse_args()

    root = Path.cwd()
    result = audit(root)
    output = root / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    print(
        "linked_images={linked} broken_links={broken} missing_local={missing} "
        "missing_new_pages={missing_pages} current_linked_images={current_linked} "
        "current_broken_links={current_broken_links} current_broken_images={current_broken_images}".format(
            linked=len(result["linked_images"]),
            broken=len(result["broken_linked_images"]),
            missing=len(result["missing_local_images"]),
            missing_pages=len(result["missing_new_pages"]),
            current_linked=len(result["current_linked_images"]),
            current_broken_links=len(result["current_broken_linked_images"]),
            current_broken_images=len(result["current_broken_image_sources"]),
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
