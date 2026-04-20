"""ტესტი სავარჯიშო 9 — find_anagrams."""
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))

from _runner import run_cases
from exercise_09_find_anagrams import find_anagrams


def check_groups(expected_groups):
    """ამოწმებს რომ ჯგუფები შეესაბამება. გარე თანმიმდევრობა არ მოწმდება,
    მაგრამ შიდა თანმიმდევრობა — კი (input-ის მიხედვით)."""
    def _check(actual):
        if not isinstance(actual, list):
            return False, f"მოლოდინი list, მიღებული: {type(actual).__name__}"
        # Normalize by sorting outer lists by first element for comparison
        try:
            actual_norm = sorted([list(g) for g in actual], key=lambda g: g[0] if g else "")
            expected_norm = sorted(expected_groups, key=lambda g: g[0] if g else "")
        except (TypeError, IndexError):
            return False, f"ჯგუფების სტრუქტურა არასწორია: {actual}"
        if actual_norm != expected_norm:
            return False, f"მოლოდინი (ჯგუფები): {expected_groups}"
        return True, ""
    return _check


cases = [
    ("find_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])",
     lambda: find_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]),
     check_groups([["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])),
    ("find_anagrams(['abc', 'bca', 'xyz', 'cab'])",
     lambda: find_anagrams(["abc", "bca", "xyz", "cab"]),
     check_groups([["abc", "bca", "cab"], ["xyz"]])),
    ("find_anagrams([]) — ცარიელი",
     lambda: find_anagrams([]),
     check_groups([])),
    ("find_anagrams(['hello']) — ერთი სიტყვა",
     lambda: find_anagrams(["hello"]),
     check_groups([["hello"]])),
    ("find_anagrams(['a', 'b', 'c']) — ყველა ცალკე",
     lambda: find_anagrams(["a", "b", "c"]),
     check_groups([["a"], ["b"], ["c"]])),
    ("find_anagrams(['listen', 'silent', 'enlist', 'google']) — 2 ჯგუფი",
     lambda: find_anagrams(["listen", "silent", "enlist", "google"]),
     check_groups([["listen", "silent", "enlist"], ["google"]])),
]

if __name__ == "__main__":
    run_cases("სავარჯიშო 9: find_anagrams", cases)
