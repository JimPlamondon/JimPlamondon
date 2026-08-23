#!/usr/bin/env python3
"""Convert YouTube caption files (.vtt / .srt) into a clean Markdown transcript.

YouTube auto-captions are written as a *rolling* two-line display: each cue
repeats the tail of the previous cue so the viewer sees a scrolling window.
Naively stripping the timestamps therefore yields every phrase two or three
times. The de-duplication below reconstructs the underlying word stream by
appending only the suffix of each cue that is genuinely new.

Usage:
    captions_to_md.py INPUT [-o OUT.md] [--title T] [--url U] [--speaker S]
                            [--every SECONDS] [--no-timestamps]
"""

from __future__ import annotations

import argparse
import html
import os
import re
import sys

# "<00:00:12.345>" inline word timings and "<c>...</c>" colour spans that
# YouTube sprinkles through auto-generated cues.
INLINE_TAG_RE = re.compile(r"<[^>]+>")
# WebVTT cue timing line, with optional trailing positioning settings.
VTT_TIME_RE = re.compile(
    r"^(\d{2}:\d{2}:\d{2}[.,]\d{3})\s*-->\s*(\d{2}:\d{2}:\d{2}[.,]\d{3})"
)
# SRT cues are preceded by a bare sequence number.
SRT_INDEX_RE = re.compile(r"^\d+$")
# Cue payload sometimes carries a "speaker:" prefix we want to keep.
SPEAKER_RE = re.compile(r"^([A-Z][A-Za-z .'-]{1,30}):\s+")


def parse_timestamp(ts: str) -> float:
    """Return seconds for an "HH:MM:SS.mmm" (or ",mmm") timestamp."""
    hh, mm, rest = ts.split(":")
    ss, _, ms = rest.replace(",", ".").partition(".")
    return int(hh) * 3600 + int(mm) * 60 + int(ss) + int(ms or 0) / 1000.0


def format_timestamp(seconds: float) -> str:
    total = int(seconds)
    hh, mm, ss = total // 3600, (total % 3600) // 60, total % 60
    return f"{hh:d}:{mm:02d}:{ss:02d}" if hh else f"{mm:d}:{ss:02d}"


def clean_line(line: str) -> str:
    line = INLINE_TAG_RE.sub("", line)
    line = html.unescape(line)
    # Collapse the runs of whitespace that tag removal leaves behind.
    return re.sub(r"\s+", " ", line).strip()


def parse_cues(text: str) -> list[tuple[float, str]]:
    """Extract (start_seconds, text) pairs from VTT or SRT content."""
    cues: list[tuple[float, str]] = []
    start: float | None = None
    buffer: list[str] = []

    def flush() -> None:
        if start is None:
            return
        body = clean_line(" ".join(buffer))
        if body:
            cues.append((start, body))

    for raw in text.splitlines():
        line = raw.strip("﻿").rstrip()
        match = VTT_TIME_RE.match(line.strip())
        if match:
            flush()
            start, buffer = parse_timestamp(match.group(1)), []
            continue
        stripped = line.strip()
        if not stripped:
            flush()
            start, buffer = None, []
            continue
        # Headers and structural noise that carry no spoken words.
        if stripped in ("WEBVTT",) or stripped.startswith(
            ("NOTE", "STYLE", "REGION", "Kind:", "Language:")
        ):
            continue
        if start is None and SRT_INDEX_RE.match(stripped):
            continue
        if start is not None:
            buffer.append(stripped)

    flush()
    return cues


def dedupe(cues: list[tuple[float, str]]) -> list[tuple[float, str]]:
    """Rebuild the word stream, dropping YouTube's rolling-window repetition.

    For each cue we find the longest prefix of its words that is already the
    suffix of what we have kept, and emit only the remainder.
    """
    words: list[str] = []
    marks: list[tuple[float, int]] = []  # (start, index into `words`)

    for start, body in cues:
        incoming = body.split()
        if not incoming:
            continue
        overlap = 0
        limit = min(len(incoming), len(words))
        for size in range(limit, 0, -1):
            if [w.lower() for w in words[-size:]] == [
                w.lower() for w in incoming[:size]
            ]:
                overlap = size
                break
        fresh = incoming[overlap:]
        if not fresh:
            continue
        marks.append((start, len(words)))
        words.extend(fresh)

    # Re-attach each surviving cue's start time to its slice of the stream.
    out: list[tuple[float, str]] = []
    for i, (start, idx) in enumerate(marks):
        end = marks[i + 1][1] if i + 1 < len(marks) else len(words)
        chunk = " ".join(words[idx:end])
        if chunk:
            out.append((start, chunk))
    return out


def to_paragraphs(
    cues: list[tuple[float, str]], every: float
) -> list[tuple[float, str]]:
    """Group cues into paragraphs, breaking on sentence ends past `every`."""
    paragraphs: list[tuple[float, str]] = []
    start: float | None = None
    parts: list[str] = []

    for ts, body in cues:
        if start is None:
            start = ts
        parts.append(body)
        elapsed = ts - start
        if elapsed >= every and re.search(r"[.!?][\"')\]]*$", body):
            paragraphs.append((start, " ".join(parts)))
            start, parts = None, []
        # Hard cap so a caption track with no punctuation still breaks.
        elif elapsed >= every * 2.5:
            paragraphs.append((start, " ".join(parts)))
            start, parts = None, []

    if parts and start is not None:
        paragraphs.append((start, " ".join(parts)))
    return paragraphs


def build_markdown(args, paragraphs: list[tuple[float, str]]) -> str:
    title = args.title or os.path.splitext(os.path.basename(args.input))[0]
    lines = [f"# {title}", ""]
    if args.url:
        lines += [f"**Source:** {args.url}", ""]
    if args.speaker:
        lines += [f"**Speaker:** {args.speaker}", ""]
    if args.url or args.speaker:
        lines += ["---", ""]

    for ts, body in paragraphs:
        prefix = "" if args.no_timestamps else f"**[{format_timestamp(ts)}]** "
        speaker = SPEAKER_RE.match(body)
        if speaker:
            body = SPEAKER_RE.sub("", body)
            prefix += f"**{speaker.group(1)}:** "
        lines += [f"{prefix}{body}", ""]

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Convert a .vtt/.srt caption file into a Markdown transcript."
    )
    parser.add_argument("input", help="caption file (.vtt or .srt)")
    parser.add_argument("-o", "--output", help="output .md (default: alongside input)")
    parser.add_argument("--title", help="document title")
    parser.add_argument("--url", help="source URL to record in the header")
    parser.add_argument("--speaker", help="speaker to record in the header")
    parser.add_argument(
        "--every",
        type=float,
        default=45.0,
        help="approximate seconds per paragraph (default: 45)",
    )
    parser.add_argument(
        "--no-timestamps", action="store_true", help="omit per-paragraph timestamps"
    )
    args = parser.parse_args()

    try:
        with open(args.input, encoding="utf-8-sig") as fh:
            text = fh.read()
    except OSError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    cues = dedupe(parse_cues(text))
    if not cues:
        print("error: no caption cues found", file=sys.stderr)
        return 1

    markdown = build_markdown(args, to_paragraphs(cues, args.every))
    out = args.output or os.path.splitext(args.input)[0] + ".md"
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(markdown)

    words = sum(len(body.split()) for _, body in cues)
    print(f"wrote {out} ({words} words, {len(cues)} cues)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
