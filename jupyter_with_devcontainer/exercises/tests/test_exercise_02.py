"""ტესტი სავარჯიშო 2 — is_even."""
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))

from _runner import run_cases
from exercise_02_is_even import is_even

cases = [
    ("is_even(4) → True", lambda: is_even(4), True),
    ("is_even(7) → False", lambda: is_even(7), False),
    ("is_even(0) → True", lambda: is_even(0), True),
    ("is_even(-2) → True", lambda: is_even(-2), True),
    ("is_even(1) → False", lambda: is_even(1), False),
    ("is_even(100) → True", lambda: is_even(100), True),
    ("is_even(-7) → False", lambda: is_even(-7), False),
]

if __name__ == "__main__":
    run_cases("სავარჯიშო 2: is_even", cases)
