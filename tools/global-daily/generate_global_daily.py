#!/usr/bin/env python3
"""Prepare the daily 08:00 WeChat issue bundle of 《环球日报》."""

from __future__ import annotations

import argparse
import copy
import html
import json
import re
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime, timedelta
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any
from urllib.parse import urlparse
from zoneinfo import ZoneInfo


DEFAULT_CONFIG = {
    "timezone": "Asia/Shanghai",
    "publish_time": "08:00",
    "hours_back": 36,
    "max_items_per_feed": 8,
    "max_total_items": 24,
    "max_discovery_items": 4,
    "min_editorial_score": 18,
    "role_min_scores": {
        "official": 30,
        "bridge": 30,
        "international": 23,
        "business": 26,
        "tech": 36,
        "science": 24,
        "discovery": 0,
    },
    "source_min_scores": {
        "BBC World": 28,
        "BBC Chinese": 28,
        "Federal Reserve Press Releases": 22,
        "Federal Reserve Monetary Policy": 24,
        "Federal Reserve Policy Rates": 24,
        "SCMP": 26,
        "虎嗅": 32,
        "钛媒体": 34,
        "华尔街见闻": 26,
    },
    "role_caps": {
        "official": 8,
        "bridge": 4,
        "international": 5,
        "business": 5,
        "tech": 3,
        "science": 2,
        "discovery": 4,
    },
    "cover_path": "../assets/global-daily-cover.svg",
    "wechat_publish": {
        "theme": "lapis",
        "highlight": "solarized-light",
    },
    "feeds": [
        {
            "name": "新华社新闻_新华网",
            "url": "https://plink.anyfeeder.com/newscn/whxw",
            "role": "official",
            "max_items": 6,
        },
        {
            "name": "人民日报",
            "url": "https://plink.anyfeeder.com/people-daily",
            "role": "official",
            "max_items": 3,
        },
        {
            "name": "《联合早报》-中港台-即时",
            "url": "https://plink.anyfeeder.com/zaobao/realtime/china",
            "role": "bridge",
            "max_items": 3,
        },
        {
            "name": "《联合早报》-国际-即时",
            "url": "https://plink.anyfeeder.com/zaobao/realtime/world",
            "role": "bridge",
            "max_items": 3,
        },
        {
            "name": "BBC World",
            "url": "https://feeds.bbci.co.uk/news/world/rss.xml",
            "role": "international",
            "max_items": 3,
        },
        {
            "name": "BBC Business",
            "url": "https://feeds.bbci.co.uk/news/business/rss.xml",
            "role": "international",
            "max_items": 2,
        },
        {
            "name": "SCMP",
            "url": "https://www.scmp.com/rss/91/feed/",
            "role": "international",
            "max_items": 2,
        },
        {
            "name": "纽约时报中文网 国际纵览",
            "url": "http://cn.nytimes.com/rss/news.xml",
            "role": "bridge",
            "max_items": 2,
        },
        {
            "name": "BBC Chinese",
            "url": "https://feeds.bbci.co.uk/zhongwen/trad/rss.xml",
            "role": "bridge",
            "max_items": 2,
        },
        {
            "name": "Federal Reserve Press Releases",
            "url": "https://www.federalreserve.gov/feeds/press_all.xml",
            "role": "international",
            "max_items": 1,
        },
        {
            "name": "Federal Reserve Monetary Policy",
            "url": "https://www.federalreserve.gov/feeds/press_monetary.xml",
            "role": "international",
            "max_items": 1,
        },
        {
            "name": "Federal Reserve Policy Rates",
            "url": "https://www.federalreserve.gov/feeds/prates.xml",
            "role": "international",
            "max_items": 1,
        },
        {
            "name": "财新网",
            "url": "https://plink.anyfeeder.com/weixin/caixinwang",
            "role": "business",
            "max_items": 3,
        },
        {
            "name": "华尔街见闻",
            "url": "https://plink.anyfeeder.com/weixin/wallstreetcn",
            "role": "business",
            "max_items": 2,
        },
        {
            "name": "界面新闻: 商业",
            "url": "https://plink.anyfeeder.com/jiemian/business",
            "role": "business",
            "max_items": 2,
        },
        {
            "name": "36氪",
            "url": "https://www.36kr.com/feed",
            "role": "tech",
            "max_items": 2,
        },
        {
            "name": "虎嗅",
            "url": "https://rss.huxiu.com/",
            "role": "tech",
            "max_items": 1,
        },
        {
            "name": "钛媒体",
            "url": "https://www.tmtpost.com/feed",
            "role": "tech",
            "max_items": 1,
        },
        {
            "name": "IT之家",
            "url": "https://www.ithome.com/rss/",
            "role": "tech",
            "max_items": 2,
        },
        {
            "name": "果壳网 科学人",
            "url": "https://plink.anyfeeder.com/guokr/scientific",
            "role": "science",
            "max_items": 1,
        },
        {
            "name": "Google News: Reuters Search",
            "url": "https://news.google.com/rss/search?q=site%3Areuters.com&hl=en-US&gl=US&ceid=US%3Aen",
            "role": "discovery",
            "max_items": 4,
            "discovery_only": True,
            "required_publisher": "Reuters",
        },
    ],
}

BUNDLE_SCHEMA_VERSION = "global-daily.bundle/v1"


def deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    merged = copy.deepcopy(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = deep_merge(merged[key], value)
        else:
            merged[key] = value
    return merged


def strip_tags(raw: str) -> str:
    text = re.sub(r"<[^>]+>", " ", raw or "")
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def clean_summary(raw: str) -> str:
    text = strip_tags(raw)
    for marker in SUMMARY_TRUNCATION_MARKERS:
        index = text.find(marker)
        if index != -1:
            text = text[:index]
    for pattern in SUMMARY_TRIM_PATTERNS:
        text = re.sub(pattern, "", text, flags=re.IGNORECASE)
    return re.sub(r"\s+", " ", text).strip()


def slugify(value: str) -> str:
    lowered = value.lower()
    lowered = re.sub(r"[^a-z0-9]+", "-", lowered)
    lowered = lowered.strip("-")
    return lowered or "item"


@dataclass
class FeedItem:
    source: str
    title: str
    link: str
    published_at: datetime | None
    summary: str
    publisher: str = ""
    author: str = ""
    role: str = "general"
    editorial_score: int = 0
    discovery_only: bool = False


ROLE_BASE_SCORES = {
    "official": 16,
    "bridge": 14,
    "international": 13,
    "business": 12,
    "tech": 7,
    "science": 9,
    "discovery": 6,
    "general": 10,
}

STRONG_SIGNAL_KEYWORDS = (
    "国务院",
    "国办",
    "实施方案",
    "信用",
    "监管",
    "调查",
    "伊朗",
    "中东",
    "油价",
    "关税",
    "导弹",
    "发射装置",
    "利率",
    "汇率",
    "通胀",
    "联储",
    "美联储",
    "经济",
    "市场",
    "出口",
    "稀土",
    "能源",
    "光伏",
    "存储芯片",
    "内存",
    "涨价",
    "企业",
    "平台",
    "评价体系",
    "数据",
)

MEDIUM_SIGNAL_KEYWORDS = (
    "特朗普",
    "Trump",
    "Fed",
    "Federal Reserve",
    "interest rate",
    "policy rate",
    "monetary policy",
    "Beige Book",
    "AI",
    "算力",
    "Agent",
    "新能源",
    "制造",
    "汽车",
    "手机",
    "价格",
    "消费",
    "产业",
    "市场监管",
    "航运",
    "供应链",
)

OPINION_TITLE_PATTERNS = (
    r"有感",
    r"专访",
    r"对话",
    r"road\s*trip",
    r"短板吗",
    r"还是一门.+吗",
    r"只剩两种公司",
    r"如何把",
    r"喊话",
    r"现场评论",
    r"大数据观察",
    r"共同关注",
    r"读者点题",
    r"钛晨报",
    r"汽车早报",
    r"^watch:",
)

OPINION_SUMMARY_PATTERNS = (
    r"本文来自微信公众号",
    r"作者：",
    r"第一人称",
    r"我读了全文",
)

PRODUCT_PR_TITLE_PATTERNS = (
    r"游戏本",
    r"车型",
    r"配置公布",
    r"限量登场",
    r"接入",
    r"首发",
    r"上架",
    r"推出",
    r"盲订",
    r"评测",
    r"真机",
)

SOFT_FEATURE_TITLE_PATTERNS = (
    r"一场花事",
    r"有群",
    r"树立和践行",
    r"从.+到.+",
    r"搬到一线",
)

BRIDGE_SOFT_TITLE_PATTERNS = (
    r"影评",
    r"感覺更好",
    r"感觉更好",
    r"你能怎麼做",
    r"你能怎么做",
    r"孩子刷手機",
    r"孩子刷手机",
    r"護膚",
    r"护肤",
    r"皮膚有什麼影響",
    r"皮肤有什么影响",
)

KR_SOFT_TITLE_PATTERNS = (
    r"创造营",
    r"一款.+游戏",
    r"活力依旧",
    r"运营三年",
    r"背后[:：]",
)

SCMP_LOW_SIGNAL_LINK_PATTERNS = (
    r"/news/hong-kong/(law-and-crime|health-environment|transport|society|education|community)/",
    r"/lifestyle/",
    r"/sport/",
    r"/comment/",
    r"/opinion/",
    r"/video/",
    r"/magazines/",
)

SCMP_WIRE_BYLINES = {
    "Associated Press",
    "Agence France-Presse",
    "Bloomberg",
    "Reuters",
}

PROMOTIONAL_TITLE_PATTERNS = (
    r"新蓝海",
    r"新图景",
    r"新空间",
    r"请就位",
    r"准备好了吗",
    r"最后一根稻草",
    r"涨到多少",
    r"考验还没完",
    r"赛道",
)

LOW_SIGNAL_TITLE_PATTERNS = (
    r"\bmarriage\b",
    r"\bbaby\b",
    r"shot dead",
    r"police say",
    r"inelegant",
    r"epstein",
    r"attorney general",
    r"watch:",
)

COMMENTARY_STYLE_TITLE_PATTERNS = (
    r"炸出",
    r"祖师爷",
    r"打醒",
    r"停止幻想",
    r"风声鹤唳",
)

DIGEST_TITLE_PATTERNS = (
    r"一周出海参考",
    r"一周.+参考",
    r"周报",
    r"晨报",
    r"早报",
    r"盘前要闻一览",
)

FED_LOW_VALUE_TITLE_PATTERNS = (
    r"enforcement action",
    r"cease and desist",
    r"civil money penalty",
)

VIDEO_STUB_SUMMARY_PATTERNS = (
    r"新华社音视频部制作",
    r"记者：.+编导：",
)

DISALLOWED_LINK_HOSTS = {
    "weixin.sogou.com",
}

NON_ARTICLE_LINK_PATTERNS = (
    r"/videos?/",
    r"/sounds/",
    r"/iplayer/",
    r"/sport/",
)

DATE_IN_LINK_PATTERNS = (
    r"/(20\d{2})/(\d{2})/(\d{2})/",
    r"/(20\d{2})(\d{2})(\d{2})/",
    r"content_(20\d{2})(\d{2})(\d{2})",
)

SUMMARY_TRUNCATION_MARKERS = (
    "/enpproperty",
    "Copyright ©",
    "document.write(",
    "function updateMetaRmrb",
)

SUMMARY_TRIM_PATTERNS = (
    r"\s20\d{2}-\d{2}-\d{2}\s00:00:00:0.*$",
    r"\shttps?://paper\.people\.com\.cn/.*$",
)

TITLE_PREFIX_PATTERNS = (
    r"^新华社消息[丨｜:：]\s*",
    r"^新华社快讯[丨｜:：]\s*",
    r"^快讯[丨｜:：]\s*",
)

FALLBACK_DATE_FORMATS = (
    "%Y-%m-%d %H:%M:%S %z",
    "%Y-%m-%d %H:%M:%S",
)


def load_config(tool_dir: Path) -> dict[str, Any]:
    config = copy.deepcopy(DEFAULT_CONFIG)
    config_path = tool_dir / "config.json"
    if config_path.exists():
        user_config = json.loads(config_path.read_text(encoding="utf-8"))
        config = deep_merge(config, user_config)
    return config


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Prepare the 08:00 issue bundle of 《环球日报》.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Write prompt and sources, plus a placeholder article for inspection.",
    )
    parser.add_argument(
        "--print-prompt",
        action="store_true",
        help="Print the drafting prompt to stdout after writing the local bundle files.",
    )
    parser.add_argument(
        "--print-manifest",
        action="store_true",
        help="Print the bundle manifest JSON to stdout after writing the local bundle files.",
    )
    parser.add_argument(
        "--as-of",
        help="Override generation timestamp in ISO-8601 format. Defaults to now.",
    )
    return parser.parse_args()


def resolve_now(config: dict[str, Any], as_of: str | None) -> datetime:
    tz = ZoneInfo(config["timezone"])
    if as_of:
        parsed = datetime.fromisoformat(as_of)
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=tz)
        return parsed.astimezone(tz)
    return datetime.now(tz)


def fetch_bytes(url: str) -> bytes:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "agent-helpdesk global-daily/1.0",
            "Accept": "application/rss+xml, application/xml, text/xml;q=0.9, */*;q=0.8",
        },
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        return response.read()


def parse_date(value: str | None, timezone_name: str) -> datetime | None:
    if not value:
        return None
    normalized = re.sub(r"\s+", " ", value).strip()
    try:
        parsed = parsedate_to_datetime(normalized)
    except (TypeError, ValueError, IndexError):
        parsed = None
    if parsed is None:
        for date_format in FALLBACK_DATE_FORMATS:
            try:
                parsed = datetime.strptime(normalized, date_format)
                break
            except ValueError:
                continue
    if parsed is None:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=ZoneInfo(timezone_name))
    return parsed.astimezone(ZoneInfo(timezone_name))


def parse_feed(feed: dict[str, Any], timezone_name: str) -> list[FeedItem]:
    raw = fetch_bytes(feed["url"])
    root = ET.fromstring(raw)
    items: list[FeedItem] = []

    channel_items = root.findall(".//channel/item")
    if channel_items:
        for node in channel_items:
            title = strip_tags(node.findtext("title"))
            link = (node.findtext("link") or "").strip()
            summary = clean_summary(node.findtext("description") or "")
            published_at = parse_date(node.findtext("pubDate"), timezone_name)
            source_node = node.find("source")
            publisher = strip_tags(source_node.text or "") if source_node is not None and source_node.text else ""
            author = strip_tags(
                node.findtext("author")
                or node.findtext("{http://purl.org/dc/elements/1.1/}creator")
                or ""
            )
            if title and link:
                items.append(
                    FeedItem(
                        source=feed["name"],
                        title=title,
                        link=link,
                        published_at=published_at,
                        summary=summary,
                        publisher=publisher,
                        author=author,
                        role=feed.get("role", "general"),
                        discovery_only=bool(feed.get("discovery_only", False)),
                    )
                )
        return items

    namespace = {"atom": "http://www.w3.org/2005/Atom"}
    atom_entries = root.findall(".//atom:entry", namespace)
    for node in atom_entries:
        title = strip_tags(node.findtext("atom:title", default="", namespaces=namespace))
        link = ""
        for link_node in node.findall("atom:link", namespace):
            href = (link_node.get("href") or "").strip()
            rel = (link_node.get("rel") or "alternate").strip()
            if href and rel == "alternate":
                link = href
                break
        summary = strip_tags(
            node.findtext("atom:summary", default="", namespaces=namespace)
            or node.findtext("atom:content", default="", namespaces=namespace)
        )
        summary = clean_summary(summary)
        source_node = node.find("source")
        publisher = strip_tags(source_node.text or "") if source_node is not None and source_node.text else ""
        author = strip_tags(node.findtext("atom:author/atom:name", default="", namespaces=namespace))
        published_raw = (
            node.findtext("atom:updated", default="", namespaces=namespace)
            or node.findtext("atom:published", default="", namespaces=namespace)
        )
        published_at = parse_date(published_raw, timezone_name)
        if title and link:
            items.append(
                FeedItem(
                    source=feed["name"],
                    title=title,
                    link=link,
                    published_at=published_at,
                    summary=summary,
                    publisher=publisher,
                    author=author,
                    role=feed.get("role", "general"),
                    discovery_only=bool(feed.get("discovery_only", False)),
                )
            )
    return items


def clean_title(title: str) -> str:
    cleaned = re.sub(r"^\d+版\s*-\s*", "", title).strip()
    return re.sub(r"\s+", " ", cleaned)


def count_keyword_hits(text: str, keywords: tuple[str, ...]) -> int:
    return sum(1 for keyword in keywords if keyword in text)


def matches_any_pattern(text: str, patterns: tuple[str, ...]) -> bool:
    return any(re.search(pattern, text, flags=re.IGNORECASE) for pattern in patterns)


def link_hostname(url: str) -> str:
    if not url:
        return ""
    return (urlparse(url).hostname or "").lower()


def is_disallowed_link(url: str) -> bool:
    hostname = link_hostname(url)
    return hostname in DISALLOWED_LINK_HOSTS


def is_non_article_link(url: str) -> bool:
    return any(re.search(pattern, url, flags=re.IGNORECASE) for pattern in NON_ARTICLE_LINK_PATTERNS)


def infer_date_from_link(url: str, timezone_name: str) -> datetime | None:
    if not url:
        return None
    for pattern in DATE_IN_LINK_PATTERNS:
        matched = re.search(pattern, url)
        if not matched:
            continue
        year, month, day = (int(part) for part in matched.groups())
        try:
            return datetime(year, month, day, tzinfo=ZoneInfo(timezone_name))
        except ValueError:
            return None
    return None


def resolve_item_timestamp(item: FeedItem, timezone_name: str) -> datetime | None:
    return item.published_at or infer_date_from_link(item.link, timezone_name)


def canonical_title_key(source: str, title: str) -> str:
    normalized = title
    for pattern in TITLE_PREFIX_PATTERNS:
        normalized = re.sub(pattern, "", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"[\s:：\-—|丨｜]+", "", normalized)
    return f"{source}:{normalized.lower()}"


def normalize_item_title(item: FeedItem) -> str:
    title = clean_title(item.title)
    if item.publisher and title.endswith(f" - {item.publisher}"):
        title = title[: -(len(item.publisher) + 3)].strip()
    return title


def score_item(item: FeedItem, now: datetime) -> int:
    text = f"{item.title} {item.summary}"
    score = ROLE_BASE_SCORES.get(item.role, ROLE_BASE_SCORES["general"])

    title_strong_hits = count_keyword_hits(item.title, STRONG_SIGNAL_KEYWORDS)
    title_medium_hits = count_keyword_hits(item.title, MEDIUM_SIGNAL_KEYWORDS)
    summary_strong_hits = count_keyword_hits(item.summary, STRONG_SIGNAL_KEYWORDS)
    summary_medium_hits = count_keyword_hits(item.summary, MEDIUM_SIGNAL_KEYWORDS)
    score += min(title_strong_hits, 3) * 9
    score += min(title_medium_hits, 2) * 4
    score += min(summary_strong_hits, 2) * 2
    score += min(summary_medium_hits, 2) * 1

    if item.published_at:
        age_hours = (now - item.published_at).total_seconds() / 3600
        if age_hours <= 6:
            score += 6
        elif age_hours <= 12:
            score += 4
        elif age_hours <= 24:
            score += 2

    if title_strong_hits == 0 and title_medium_hits == 0:
        score -= 14
    if matches_any_pattern(item.title, OPINION_TITLE_PATTERNS):
        score -= 18
    if matches_any_pattern(text, OPINION_SUMMARY_PATTERNS):
        score -= 18
    if matches_any_pattern(item.title, PRODUCT_PR_TITLE_PATTERNS):
        score -= 14
    if matches_any_pattern(item.title, SOFT_FEATURE_TITLE_PATTERNS):
        score -= 10
    if item.role == "bridge" and matches_any_pattern(item.title, BRIDGE_SOFT_TITLE_PATTERNS):
        score -= 14
    if item.source == "36氪" and matches_any_pattern(item.title, KR_SOFT_TITLE_PATTERNS):
        score -= 14
    if item.source == "36氪" and len(item.summary) > 700 and title_strong_hits == 0 and title_medium_hits <= 1:
        score -= 12
    if item.source == "SCMP" and matches_any_pattern(item.link, SCMP_LOW_SIGNAL_LINK_PATTERNS):
        score -= 20
    if item.source == "SCMP" and item.author in SCMP_WIRE_BYLINES:
        score -= 8
    if matches_any_pattern(item.title, PROMOTIONAL_TITLE_PATTERNS):
        score -= 16
    if matches_any_pattern(item.title, LOW_SIGNAL_TITLE_PATTERNS):
        score -= 18
    if matches_any_pattern(item.title, COMMENTARY_STYLE_TITLE_PATTERNS):
        score -= 18
    if matches_any_pattern(item.title, DIGEST_TITLE_PATTERNS):
        score -= 14
    if item.source.startswith("Federal Reserve") and matches_any_pattern(item.title, FED_LOW_VALUE_TITLE_PATTERNS):
        score -= 16
    if ("？" in item.title or "?" in item.title) and title_strong_hits == 0:
        score -= 10
    if "..." in item.title or "！" in item.title:
        score -= 6
    if item.role == "tech" and title_strong_hits == 0 and title_medium_hits <= 1:
        score -= 8
    if matches_any_pattern(item.summary, VIDEO_STUB_SUMMARY_PATTERNS):
        score -= 10
    if not item.summary:
        score -= 6

    return score


def collect_feed_items(config: dict[str, Any], now: datetime) -> tuple[list[FeedItem], list[FeedItem]]:
    cutoff = now - timedelta(hours=int(config["hours_back"]))
    dedupe: dict[str, FeedItem] = {}
    candidates: list[FeedItem] = []
    discovery_dedupe: dict[str, FeedItem] = {}
    discovery_candidates: list[FeedItem] = []
    role_caps: dict[str, int] = {key: int(value) for key, value in config.get("role_caps", {}).items()}
    role_min_scores: dict[str, int] = {key: int(value) for key, value in config.get("role_min_scores", {}).items()}
    source_min_scores: dict[str, int] = {key: int(value) for key, value in config.get("source_min_scores", {}).items()}
    source_caps: dict[str, int] = {}
    min_editorial_score = int(config.get("min_editorial_score", 0))

    for feed in config["feeds"]:
        try:
            parsed_items = parse_feed(feed, config["timezone"])
        except Exception as exc:
            print(f"Warning: skipping feed {feed['name']}: {exc}", file=sys.stderr)
            continue
        scored_items: list[FeedItem] = []
        discovery_items: list[FeedItem] = []
        per_feed_cap = int(feed.get("max_items", config["max_items_per_feed"]))
        source_caps[feed["name"]] = per_feed_cap
        required_publisher = str(feed.get("required_publisher", "")).strip()
        for item in parsed_items:
            item.title = normalize_item_title(item)
            item.published_at = resolve_item_timestamp(item, config["timezone"])
            if is_disallowed_link(item.link):
                continue
            if is_non_article_link(item.link):
                continue
            if item.published_at is None or item.published_at < cutoff:
                continue
            if required_publisher and item.publisher != required_publisher:
                continue
            item.editorial_score = score_item(item, now)
            if item.discovery_only:
                if not item.summary:
                    continue
                discovery_items.append(item)
                continue
            min_score = max(
                min_editorial_score,
                role_min_scores.get(item.role, min_editorial_score),
                source_min_scores.get(item.source, min_editorial_score),
            )
            if (
                not item.summary
                and item.role in {"bridge", "business", "tech"}
                and item.editorial_score < min_score + 6
            ):
                continue
            if item.editorial_score < min_score:
                continue
            scored_items.append(item)

        if feed.get("discovery_only"):
            kept = 0
            for item in sorted(
                discovery_items,
                key=lambda value: (value.published_at or cutoff, value.editorial_score),
                reverse=True,
            ):
                keys = {
                    item.link or slugify(item.title),
                    canonical_title_key(item.source, item.title),
                }
                if any(key in discovery_dedupe for key in keys):
                    continue
                for key in keys:
                    discovery_dedupe[key] = item
                discovery_candidates.append(item)
                kept += 1
                if kept >= per_feed_cap:
                    break
            continue
        kept = 0
        for item in sorted(
            scored_items,
            key=lambda value: (value.editorial_score, value.published_at or cutoff),
            reverse=True,
        ):
            keys = {
                item.link or slugify(item.title),
                canonical_title_key(item.source, item.title),
            }
            if any(key in dedupe for key in keys):
                continue
            for key in keys:
                dedupe[key] = item
            candidates.append(item)
            kept += 1
            if kept >= per_feed_cap:
                break

    role_counts: dict[str, int] = {}
    source_counts: dict[str, int] = {}
    selected: list[FeedItem] = []

    for item in sorted(
        candidates,
        key=lambda value: (value.editorial_score, value.published_at or cutoff),
        reverse=True,
    ):
        if role_counts.get(item.role, 0) >= role_caps.get(item.role, int(config["max_total_items"])):
            continue
        if source_counts.get(item.source, 0) >= source_caps.get(item.source, int(config["max_items_per_feed"])):
            continue
        selected.append(item)
        role_counts[item.role] = role_counts.get(item.role, 0) + 1
        source_counts[item.source] = source_counts.get(item.source, 0) + 1
        if len(selected) >= int(config["max_total_items"]):
            break

    discovery_items = sorted(
        discovery_candidates,
        key=lambda value: (value.published_at or cutoff, value.editorial_score),
        reverse=True,
    )[: int(config.get("max_discovery_items", 0))]

    return selected, discovery_items


def load_reference_text(root_dir: Path) -> str:
    refs = [
        root_dir / "skills/daily-news/references/global-daily-profile.yaml",
        root_dir / "skills/daily-news/references/global-daily-template.md",
        root_dir / "skills/daily-news/references/feed-sources.md",
        root_dir / "skills/daily-news/references/source-policy.md",
        root_dir / "skills/daily-news/references/golden-sample.md",
        root_dir / "skills/daily-news/references/global-daily-final-sample.md",
    ]
    blocks = []
    for path in refs:
        blocks.append(f"## {path.name}\n{path.read_text(encoding='utf-8').strip()}")
    return "\n\n".join(blocks)


def build_prompt(
    config: dict[str, Any],
    root_dir: Path,
    now: datetime,
    items: list[FeedItem],
    discovery_items: list[FeedItem],
) -> str:
    ref_text = load_reference_text(root_dir)
    title = f"《环球日报》｜{now.month}月{now.day}日"
    lines = []
    for item in items:
        published = item.published_at.isoformat() if item.published_at else "unknown"
        lines.append(
            "\n".join(
                [
                    f"- source: {item.source}",
                    f"  role: {item.role}",
                    f"  published_at: {published}",
                    f"  title: {item.title}",
                    f"  link: {item.link}",
                    f"  summary: {item.summary or 'n/a'}",
                ]
            )
        )

    discovery_lines = []
    for item in discovery_items:
        published = item.published_at.isoformat() if item.published_at else "unknown"
        discovery_lines.append(
            "\n".join(
                [
                    f"- source: {item.source}",
                    f"  publisher_hint: {item.publisher or 'n/a'}",
                    f"  role: {item.role}",
                    f"  published_at: {published}",
                    f"  title: {item.title}",
                    f"  link: {item.link}",
                    f"  summary: {item.summary or 'n/a'}",
                ]
            )
        )

    cover_path = config["cover_path"]
    discovery_block = ""
    if discovery_lines:
        discovery_block = f"""

Discovery-only agenda hints:
- These hints are for agenda sensing only.
- Do not cite, quote, or attribute them directly in the article.
- Use a discovery hint only when the same story is already supported by the citable feed items above.

{chr(10).join(discovery_lines)}
"""
    return f"""You are writing today's issue of 《环球日报》, the standing 08:00 China time WeChat daily news column.

Follow these local references exactly:

{ref_text}

Use this title exactly:
{title}

Write the final output as Markdown only. It must start with frontmatter:
---
title: {title}
cover: {cover_path}
---

Rules:
- Output Simplified Chinese.
- Do not include a duplicate H1 after the frontmatter title.
- Keep the fixed `《环球日报》` rhythm.
- Use only the citable feed items below for factual claims and citations. Do not invent facts.
- Cite each major item with source name and publish date.
- End with a short "today to watch" section.
- Include image suggestions only if they genuinely help.

Citable feed items:
{chr(10).join(lines)}{discovery_block}
"""

def strip_code_fences(markdown: str) -> str:
    cleaned = markdown.strip()
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```[a-zA-Z0-9_-]*\n", "", cleaned)
        cleaned = re.sub(r"\n```$", "", cleaned)
    return cleaned.strip()


def ensure_frontmatter(markdown: str, title: str, cover_path: str) -> str:
    cleaned = strip_code_fences(markdown)
    if cleaned.startswith("---\n"):
        end_index = cleaned.find("\n---\n", 4)
        if end_index != -1:
            frontmatter_text = cleaned[4:end_index]
            body = cleaned[end_index + 5 :].lstrip()

            fields: list[str] = []
            title_seen = False
            cover_seen = False

            for raw_line in frontmatter_text.splitlines():
                line = raw_line
                if line.startswith("title:"):
                    line = f"title: {title}"
                    title_seen = True
                elif line.startswith("cover:"):
                    line = f"cover: {cover_path}"
                    cover_seen = True
                fields.append(line)

            if not title_seen:
                fields.append(f"title: {title}")
            if not cover_seen:
                fields.append(f"cover: {cover_path}")

            return "---\n" + "\n".join(fields) + "\n---\n\n" + body

    frontmatter = f"---\ntitle: {title}\ncover: {cover_path}\n---\n\n"
    return frontmatter + cleaned.lstrip()


def output_path(tool_dir: Path, now: datetime) -> Path:
    return tool_dir / "out" / f"{now.strftime('%Y-%m-%d')}-global-daily.md"


def write_outputs(
    tool_dir: Path,
    now: datetime,
    publish_time: str,
    title: str,
    cover_path: str,
    prompt: str,
    items: list[FeedItem],
    discovery_items: list[FeedItem],
    markdown: str | None = None,
) -> dict[str, Any]:
    out_dir = tool_dir / "out"
    out_dir.mkdir(parents=True, exist_ok=True)
    article_path = output_path(tool_dir, now)
    prompt_path = out_dir / f"{now.strftime('%Y-%m-%d')}-global-daily.prompt.txt"
    items_path = out_dir / f"{now.strftime('%Y-%m-%d')}-global-daily.sources.json"
    discovery_path = out_dir / f"{now.strftime('%Y-%m-%d')}-global-daily.discovery.json"
    bundle_path = out_dir / f"{now.strftime('%Y-%m-%d')}-global-daily.bundle.json"

    if markdown is not None:
        article_path.write_text(markdown, encoding="utf-8")
    prompt_path.write_text(prompt, encoding="utf-8")
    items_path.write_text(
        json.dumps(
            [
                {
                    "source": item.source,
                    "publisher": item.publisher or None,
                    "author": item.author or None,
                    "role": item.role,
                    "editorial_score": item.editorial_score,
                    "title": item.title,
                    "link": item.link,
                    "published_at": item.published_at.isoformat() if item.published_at else None,
                    "summary": item.summary,
                    "discovery_only": item.discovery_only,
                }
                for item in items
            ],
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    discovery_path.write_text(
        json.dumps(
            [
                {
                    "source": item.source,
                    "publisher": item.publisher or None,
                    "author": item.author or None,
                    "role": item.role,
                    "editorial_score": item.editorial_score,
                    "title": item.title,
                    "link": item.link,
                    "published_at": item.published_at.isoformat() if item.published_at else None,
                    "summary": item.summary,
                    "discovery_only": item.discovery_only,
                }
                for item in discovery_items
            ],
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    article_status = "written" if markdown is not None else "pending"
    if markdown is not None and "生成已跳过" in markdown:
        article_status = "placeholder"
    manifest = {
        "schema_version": BUNDLE_SCHEMA_VERSION,
        "tool_name": "global-daily",
        "generated_at": now.isoformat(),
        "repo_root": str(tool_dir.parent.parent),
        "issue": {
            "date": now.strftime("%Y-%m-%d"),
            "title": title,
            "timezone": now.tzinfo.key if hasattr(now.tzinfo, "key") else str(now.tzinfo),
            "publish_time": publish_time,
            "cover_path": cover_path,
        },
        "artifacts": {
            "bundle_path": str(bundle_path),
            "prompt_path": str(prompt_path),
            "sources_path": str(items_path),
            "discovery_path": str(discovery_path),
            "article_path": str(article_path),
        },
        "drafting": {
            "mode": "host-llm",
            "article_format": "markdown",
            "frontmatter_required": True,
            "article_status": article_status,
            "selected_item_count": len(items),
            "discovery_item_count": len(discovery_items),
        },
    }
    bundle_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return manifest


def main() -> int:
    args = parse_args()
    tool_dir = Path(__file__).resolve().parent
    root_dir = tool_dir.parent.parent
    config = load_config(tool_dir)
    now = resolve_now(config, args.as_of)
    items, discovery_items = collect_feed_items(config, now)
    if not items:
        raise RuntimeError("No feed items collected; check feed availability or config")

    prompt = build_prompt(config, root_dir, now, items, discovery_items)
    title = f"《环球日报》｜{now.month}月{now.day}日"
    cover_path = config["cover_path"]

    if args.dry_run:
        markdown = ensure_frontmatter(
            "生成已跳过。请查看同目录 prompt 和 sources 文件。",
            title,
            cover_path,
        )
    else:
        markdown = None

    manifest = write_outputs(
        tool_dir,
        now,
        str(config["publish_time"]),
        title,
        cover_path,
        prompt,
        items,
        discovery_items,
        markdown,
    )
    if args.print_manifest:
        print(json.dumps(manifest, ensure_ascii=False, indent=2))
    elif args.print_prompt:
        print(f"BUNDLE_PATH={manifest['artifacts']['bundle_path']}")
        print(f"ARTICLE_PATH={manifest['artifacts']['article_path']}")
        print(f"PROMPT_PATH={manifest['artifacts']['prompt_path']}")
        print(f"SOURCES_PATH={manifest['artifacts']['sources_path']}")
        print("")
        print(prompt)
    else:
        print(manifest["artifacts"]["bundle_path"])
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except urllib.error.URLError as exc:
        print(f"Network error: {exc}", file=sys.stderr)
        raise SystemExit(1)
    except Exception as exc:  # pragma: no cover - shell-facing error path
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
