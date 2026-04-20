"""ტესტი სავარჯიშო 4 — word_count."""
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))

from _runner import run_cases
from exercise_04_word_count import word_count

cases = [
    ("word_count('hello world hello python')",
     lambda: word_count("hello world hello python"),
     {"hello": 2, "world": 1, "python": 1}),
    ("word_count('apple banana apple apple banana')",
     lambda: word_count("apple banana apple apple banana"),
     {"apple": 3, "banana": 2}),
    ("word_count('python') — ერთი სიტყვა",
     lambda: word_count("python"),
     {"python": 1}),
    ("word_count('') — ცარიელი ტექსტი",
     lambda: word_count(""),
     {}),
    ("word_count('a a a a')",
     lambda: word_count("a a a a"),
     {"a": 4}),
]

if __name__ == "__main__":
    run_cases("სავარჯიშო 4: word_count", cases)
