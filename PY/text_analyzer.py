#!/usr/bin/env python3
"""Simple text analyzer: counts words, characters and sentences."""

import argparse
import re
from collections import Counter


def analyze_text(text: str) -> dict:
    """Return statistics about the input text.

    - words: number of words (basic word tokenization)
    - characters: total characters including spaces
    - characters_no_spaces: characters excluding spaces
    - sentences: number of sentences (split on . ! ?)
    - most_common_words: top 5 words (lowercased)
    """
    # Words: include letters, numbers, apostrophes and hyphens inside words
    words = re.findall(r"\b[\w'-]+\b", text)
    num_words = len(words)

    num_chars = len(text)
    num_chars_no_spaces = len(re.sub(r"\s+", "", text))

    # Sentences: split on ., !, ? (one or more) and ignore empty parts
    sentences = [s for s in re.split(r'[.!?]+', text) if s.strip()]
    num_sentences = len(sentences)

    most_common_words = Counter(w.lower().strip("'\"" ) for w in words).most_common(5)

    return {
        "words": num_words,
        "characters": num_chars,
        "characters_no_spaces": num_chars_no_spaces,
        "sentences": num_sentences,
        "most_common_words": most_common_words,
    }


def format_report(stats: dict) -> str:
    lines = [
        f"Words: {stats['words']}",
        f"Characters (including spaces): {stats['characters']}",
        f"Characters (no spaces): {stats['characters_no_spaces']}",
        f"Sentences: {stats['sentences']}",
    ]
    if stats.get("most_common_words"):
        lines.append("Top words: " + ", ".join(f"{w}({c})" for w, c in stats["most_common_words"]))
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze text and output counts.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-t", "--text", help="Text to analyze. If omitted, will read from stdin.")
    group.add_argument("-f", "--file", help="File path to analyze.")
    args = parser.parse_args()

    if args.file:
        with open(args.file, encoding="utf-8") as fh:
            text = fh.read()
    elif args.text:
        text = args.text
    else:
        # Read a full line from input (user can paste a longer paragraph)
        text = input("Enter text to analyze: ")

    stats = analyze_text(text)
    print(format_report(stats))


if __name__ == "__main__":
    main()
