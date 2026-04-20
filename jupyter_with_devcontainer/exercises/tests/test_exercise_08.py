"""ტესტი სავარჯიშო 8 — validate_password."""
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))

from _runner import run_cases
from exercise_08_validate_password import validate_password


def check_errors(expected_errors):
    """ამოწმებს რომ დაბრუნებული list-ი შეიცავს ზუსტად იგივე error-ებს
    (თანმიმდევრობა არ აქვს მნიშვნელობა, მაგრამ დუბლიკატი არ უნდა ჰქონდეს)."""
    def _check(actual):
        if not isinstance(actual, list):
            return False, f"მოლოდინი list, მიღებული: {type(actual).__name__}"
        if sorted(actual) != sorted(expected_errors):
            return False, f"მოლოდინი: {expected_errors}"
        return True, ""
    return _check


cases = [
    ("validate_password('Password1!') — სწორი პაროლი",
     lambda: validate_password("Password1!"),
     check_errors([])),
    ("validate_password('abc') — ყველა წესი ირღვევა",
     lambda: validate_password("abc"),
     check_errors(["too_short", "no_uppercase", "no_digit", "no_special"])),
    ("validate_password('Short1!') — მხოლოდ too_short",
     lambda: validate_password("Short1!"),
     check_errors(["too_short"])),
    ("validate_password('password1!') — მხოლოდ no_uppercase",
     lambda: validate_password("password1!"),
     check_errors(["no_uppercase"])),
    ("validate_password('Password!') — მხოლოდ no_digit",
     lambda: validate_password("Password!"),
     check_errors(["no_digit"])),
    ("validate_password('Password1') — მხოლოდ no_special",
     lambda: validate_password("Password1"),
     check_errors(["no_special"])),
    ("validate_password('') — ცარიელი",
     lambda: validate_password(""),
     check_errors(["too_short", "no_uppercase", "no_digit", "no_special"])),
    ("validate_password('LongEnough!') — აკლია ციფრი",
     lambda: validate_password("LongEnough!"),
     check_errors(["no_digit"])),
    ("validate_password('Aa1@Bb2#') — ზუსტად 8 სიმბოლო, ყველა წესი სრულდება",
     lambda: validate_password("Aa1@Bb2#"),
     check_errors([])),
]

if __name__ == "__main__":
    run_cases("სავარჯიშო 8: validate_password", cases)
