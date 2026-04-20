"""ტესტი სავარჯიშო 3 — 3-ზე გაყოფადი რიცხვები."""
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))

from _runner import run_cases
from exercise_03_divisible_by_3 import divisible_by_3

EXPECTED = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]


def check_result(actual):
    if not isinstance(actual, list):
        return False, f"მოლოდინი list, მიღებული: {type(actual).__name__}"
    if actual != EXPECTED:
        return False, f"მოლოდინი: {EXPECTED}"
    return True, ""


cases = [
    ("divisible_by_3() აბრუნებს 1-50 შუალედიდან 3-ზე გაყოფადებს",
     divisible_by_3, check_result),
]

if __name__ == "__main__":
    run_cases("სავარჯიშო 3: 3-ზე გაყოფადი რიცხვები", cases)
