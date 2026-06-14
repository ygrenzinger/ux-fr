#!/usr/bin/env python3
"""Recover full-size linked image targets from ux-fr.com."""

from __future__ import annotations

import json
import urllib.parse
import urllib.request
from pathlib import Path


SOURCE_HOST = "https://ux-fr.com"


def fetch(url: str) -> tuple[bytes, str]:
    request = urllib.request.Request(url, headers={"User-Agent": "ux-fr-link-recovery/1.0"})
    with urllib.request.urlopen(request, timeout=20) as response:
        content_type = response.headers.get("content-type", "")
        return response.read(), content_type


def main() -> int:
    root = Path.cwd()
    audit = json.loads((root / "docs/linked-image-audit.json").read_text(encoding="utf-8"))
    recovered = 0
    failed: list[tuple[str, str]] = []
    seen: set[str] = set()

    for record in audit["current_broken_linked_images"]:
        parsed = urllib.parse.urlparse(record["href"])
        if not parsed.path.startswith("/ux-fr/wp-content/"):
            continue
        target_path = parsed.path.removeprefix("/ux-fr")
        if target_path in seen:
            continue
        seen.add(target_path)

        source_url = SOURCE_HOST + target_path
        destination = root / "static" / target_path.lstrip("/")
        try:
            body, content_type = fetch(source_url)
            if not content_type.startswith("image/"):
                failed.append((target_path, f"not an image: {content_type}"))
                continue
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(body)
            recovered += 1
            print(f"recovered {target_path} from {source_url}")
        except Exception as exc:  # noqa: BLE001 - report and continue.
            failed.append((target_path, str(exc)))

    print(f"recovered={recovered} failed={len(failed)}")
    for path, error in failed:
        print(f"failed {path}: {error}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
