"""ტესტი სავარჯიშო 5 — flatten."""
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))

from _runner import run_cases
from exercise_05_flatten import flatten

cases = [
    ("flatten([[1, 2], [3, 4], [5]])",
     lambda: flatten([[1, 2], [3, 4], [5]]),
     [1, 2, 3, 4, 5]),
    ("flatten([[1], [2, 3, 4], []])",
     lambda: flatten([[1], [2, 3, 4], []]),
     [1, 2, 3, 4]),
    ("flatten([]) — ცარიელი სია",
     lambda: flatten([]),
     []),
    ("flatten([[], [], []]) — სამი ცარიელი სია",
     lambda: flatten([[], [], []]),
     []),
    ("flatten([['a', 'b'], ['c']])",
     lambda: flatten([['a', 'b'], ['c']]),
     ['a', 'b', 'c']),
]

if __name__ == "__main__":
    run_cases("სავარჯიშო 5: flatten", cases)
