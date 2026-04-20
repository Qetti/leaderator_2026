"""ტესტი სავარჯიშო 1 — მისალმება."""
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))

from _runner import run_cases
from exercise_01_greeting import greet

cases = [
    ("greet('ანა', 25)", lambda: greet("ანა", 25),
     "გამარჯობა, ანა! 75 წლის შემდეგ 100 წლის გახდები."),
    ("greet('გიო', 0)", lambda: greet("გიო", 0),
     "გამარჯობა, გიო! 100 წლის შემდეგ 100 წლის გახდები."),
    ("greet('Alex', 50)", lambda: greet("Alex", 50),
     "გამარჯობა, Alex! 50 წლის შემდეგ 100 წლის გახდები."),
    ("greet('მარი', 99)", lambda: greet("მარი", 99),
     "გამარჯობა, მარი! 1 წლის შემდეგ 100 წლის გახდები."),
]

if __name__ == "__main__":
    run_cases("სავარჯიშო 1: მისალმება", cases)
