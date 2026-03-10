#!/usr/bin/env python3
"""
Lint a WeChat short-fiction Markdown draft for packaging and basic editorial issues.
No third-party dependencies.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from urllib.parse import urlparse

TITLE_PATTERN = re.compile(r"^《短篇小说｜\d{4}\.\d{2}\.\d{2}｜.+》$")
FRONTMATTER_PATTERN = re.compile(r"^\ufeff?\s*---\r?\n(.*?)\r?\n---\r?\n?", re.DOTALL)
LIST_OR_HEADING_PATTERN = re.compile(r"^\s*(#{1,6}\s|\d+\.\s|[-*]\s)")
CHINESE_CHAR_PATTERN = re.compile(r"[\u3400-\u9fff]")

META_PHRASES = [
    "以下是成稿",
    "可直接发布",
    "写作说明",
    "发布建议",
    "创作思路",
]

FLAGGED_PHRASES = [
    "命运跟",
    "那一刻时间仿佛静止",
    "她突然明白",
    "他突然明白",
    "原来每个人都有自己的苦衷",
    "这就是生活",
    "某种意义上",
]

ABSTRACT_TITLE_TERMS = [
    "人生",
    "成长",
    "命运",
    "真相",
    "救赎",
    "孤独",
]

SCENE_TOKENS = [
    "门",
    "灯",
    "雨",
    "电梯",
    "桌",
    "手机",
    "伞",
    "站台",
    "窗",
    "钥匙",
    "鞋",
    "屏幕",
    "走廊",
    "楼道",
    "餐盒",
    "冰箱",
    "公交",
    "便利店",
    "工牌",
    "外卖",
]

VARIANT_TARGETS = {
    "default": (1000, 1800),
    "extended": (1800, 2800),
    "flash": (700, 1000),
    "serial": (1000, 1800),
}


def parse_frontmatter(text: str) -> tuple[dict[str, str], str, str | None]:
    match = FRONTMATTER_PATTERN.match(text)
    if not match:
        return {}, text, "missing YAML frontmatter"

    frontmatter_text = match.group(1)
    body = text[match.end() :].strip()
    data: dict[str, str] = {}

    for raw_line in frontmatter_text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if raw_line.startswith((" ", "\t")):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")

    return data, body, None


def chinese_char_count(text: str) -> int:
    return len(CHINESE_CHAR_PATTERN.findall(text))


def validate_cover(cover: str, article_path: Path) -> str | None:
    parsed = urlparse(cover)
    if parsed.scheme in {"http", "https"}:
        return None

    if parsed.scheme and not cover.startswith(("/", "./", "../", "~")):
        return f"cover uses unsupported scheme `{parsed.scheme}`"

    if cover.startswith("~"):
        cover_path = Path(cover).expanduser()
    else:
        raw_path = Path(cover)
        cover_path = raw_path if raw_path.is_absolute() else (article_path.parent / raw_path)

    if not cover_path.exists():
        return f"cover path does not exist: {cover}"
    if cover_path.is_dir():
        return f"cover path points to a directory: {cover}"
    return None


def focus_from_title(title: str) -> str:
    parts = title.strip("《》").split("｜")
    if len(parts) < 3:
        return ""
    return parts[2].strip("》")


def print_issues(label: str, issues: list[str]) -> None:
    for issue in issues:
        print(f"{label}: {issue}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Lint a WeChat short-fiction Markdown draft.")
    parser.add_argument("path", help="Path to the Markdown story file")
    parser.add_argument(
        "--allow-custom-title",
        action="store_true",
        help="Allow titles that do not follow the default archive pattern",
    )
    parser.add_argument(
        "--variant",
        choices=sorted(VARIANT_TARGETS),
        default="default",
        help="Target length profile for the draft",
    )
    args = parser.parse_args()

    path = Path(args.path).resolve()
    if not path.exists():
        print(f"FAIL: file not found: {path}")
        return 1

    text = path.read_text(encoding="utf-8")
    frontmatter, body, error = parse_frontmatter(text)

    failures: list[str] = []
    warnings: list[str] = []

    if error:
        failures.append(error)
    else:
        title = frontmatter.get("title", "")
        cover = frontmatter.get("cover", "")

        if not title:
            failures.append("frontmatter missing `title`")
        elif not args.allow_custom_title and not TITLE_PATTERN.match(title):
            failures.append("title does not match the default `《短篇小说｜YYYY.MM.DD｜篇名》` pattern")

        if not cover:
            failures.append("frontmatter missing `cover`")
        else:
            cover_error = validate_cover(cover, path)
            if cover_error:
                failures.append(cover_error)

        if title:
            focus = focus_from_title(title)
            if focus and any(term in focus for term in ABSTRACT_TITLE_TERMS):
                warnings.append("title focus looks abstract; prefer an object, action, place, or line")

    if not body.strip():
        failures.append("story body is empty")

    body_lines = [line for line in body.splitlines() if line.strip()]
    for line in body_lines:
        if LIST_OR_HEADING_PATTERN.match(line):
            failures.append("body contains a heading or list marker; keep the story as continuous prose")
            break

    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", body) if p.strip()]
    paragraph_count = len(paragraphs)
    if paragraph_count < 4 or paragraph_count > 12:
        failures.append(f"paragraph count {paragraph_count} is outside the supported range 4-12")
    elif paragraph_count < 5 or paragraph_count > 9:
        warnings.append(f"paragraph count {paragraph_count} is outside the preferred range 5-9")

    target_min, target_max = VARIANT_TARGETS[args.variant]
    count = chinese_char_count(body)
    if count < 700 or count > 3200:
        failures.append(f"Chinese character count {count} is outside the supported range 700-3200")
    elif count < target_min or count > target_max:
        warnings.append(
            f"Chinese character count {count} is outside the `{args.variant}` target range {target_min}-{target_max}"
        )

    if paragraphs:
        average_len = count // len(paragraphs)
        if average_len > 340:
            warnings.append("paragraphs may be too long for phone reading; consider shorter blocks")

    for phrase in META_PHRASES:
        if phrase in body:
            failures.append(f"body contains meta phrase `{phrase}`")

    flagged_hits = [phrase for phrase in FLAGGED_PHRASES if phrase in body]
    if flagged_hits:
        warnings.append("body contains flagged cliche phrasing: " + ", ".join(flagged_hits))

    opening_window = body[:160]
    if opening_window and not any(token in opening_window for token in SCENE_TOKENS):
        warnings.append("opening may be too abstract; consider adding a clearer place, object, or action")

    if paragraphs:
        ending = paragraphs[-1].strip()
        if re.match(r"^(所以|其实|我们都|也许|原来)", ending):
            warnings.append("ending opens like an explanation; consider landing on residue or action instead")

    print(f"File: {path}")
    print(f"Variant: {args.variant}")
    print(f"Chinese chars: {count}")
    print(f"Paragraphs: {paragraph_count}")
    print_issues("FAIL", failures)
    print_issues("WARN", warnings)

    if failures:
        print("RESULT: FAIL")
        return 1

    if warnings:
        print("RESULT: WARN")
        return 0

    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
