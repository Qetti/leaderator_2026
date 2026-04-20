"""ტესტი სავარჯიშო 7 — roman_to_int."""
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))

from _runner import run_cases
from exercise_07_roman_to_int import roman_to_int

cases = [
    ("roman_to_int('I') → 1", lambda: roman_to_int("I"), 1),
    ("roman_to_int('III') → 3", lambda: roman_to_int("III"), 3),
    ("roman_to_int('IV') → 4 (დაკლება)", lambda: roman_to_int("IV"), 4),
    ("roman_to_int('IX') → 9", lambda: roman_to_int("IX"), 9),
    ("roman_to_int('LVIII') → 58", lambda: roman_to_int("LVIII"), 58),
    ("roman_to_int('XL') → 40", lambda: roman_to_int("XL"), 40),
    ("roman_to_int('XC') → 90", lambda: roman_to_int("XC"), 90),
    ("roman_to_int('CD') → 400", lambda: roman_to_int("CD"), 400),
    ("roman_to_int('MCMXCIV') → 1994", lambda: roman_to_int("MCMXCIV"), 1994),
    ("roman_to_int('MMXXIV') → 2024", lambda: roman_to_int("MMXXIV"), 2024),
    ("roman_to_int('M') → 1000", lambda: roman_to_int("M"), 1000),
]

if __name__ == "__main__":
    run_cases("სავარჯიშო 7: roman_to_int", cases)
