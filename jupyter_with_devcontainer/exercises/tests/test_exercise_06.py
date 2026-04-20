"""ტესტი სავარჯიშო 6 — სტუდენტების ანალიზი."""
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))

from _runner import run_cases
from exercise_06_students import analyze_students

STUDENTS = [
    {"name": "ანა",  "score": 75},
    {"name": "ნიკა", "score": 92},
    {"name": "გიო",  "score": 45},
    {"name": "მარი", "score": 38},
    {"name": "ლუკა", "score": 72},
]


def check_full_result(actual):
    if not isinstance(actual, dict):
        return False, f"მოლოდინი dict, მიღებული: {type(actual).__name__}"
    errors = []
    expected_avg = (75 + 92 + 45 + 38 + 72) / 5  # 64.4
    if "average" not in actual:
        errors.append("key 'average' აკლია")
    elif abs(actual["average"] - expected_avg) > 0.01:
        errors.append(f"average: მოლოდინი {expected_avg}, მიღებული {actual['average']}")
    if actual.get("top") != "ნიკა":
        errors.append(f"top: მოლოდინი 'ნიკა', მიღებული {actual.get('top')!r}")
    failed = actual.get("failed", [])
    if sorted(failed) != sorted(["გიო", "მარი"]):
        errors.append(f"failed: მოლოდინი ['გიო', 'მარი'], მიღებული {failed!r}")
    if errors:
        return False, " | ".join(errors)
    return True, ""


def check_all_passing(actual):
    """ყველა სტუდენტი > 50, 'failed' უნდა იყოს ცარიელი list."""
    if not isinstance(actual, dict):
        return False, f"მოლოდინი dict, მიღებული: {type(actual).__name__}"
    if actual.get("failed") != []:
        return False, f"failed უნდა იყოს []: მიღებული {actual.get('failed')!r}"
    if actual.get("top") != "ლაშა":
        return False, f"top: მოლოდინი 'ლაშა', მიღებული {actual.get('top')!r}"
    return True, ""


cases = [
    ("analyze_students(5 სტუდენტი, 2 ჩაჭრილი)",
     lambda: analyze_students(STUDENTS),
     check_full_result),
    ("analyze_students(ყველა გადასულია)",
     lambda: analyze_students([
         {"name": "ლაშა", "score": 88},
         {"name": "მარი", "score": 72},
         {"name": "გია",  "score": 65},
     ]),
     check_all_passing),
]

if __name__ == "__main__":
    run_cases("სავარჯიშო 6: სტუდენტების ანალიზი", cases)
