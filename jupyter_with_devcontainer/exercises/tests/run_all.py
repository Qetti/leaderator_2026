"""ყველა ტესტის გაშვება ერთად.

გაშვება:
    python tests/run_all.py
"""
import importlib
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))

from _runner import BOLD, GREEN, RED, RESET, YELLOW, run_cases  # noqa: E402


def main() -> int:
    test_modules = sorted(p.stem for p in HERE.glob("test_exercise_*.py"))
    results: list[tuple[str, bool]] = []

    for mod_name in test_modules:
        mod = importlib.import_module(mod_name)
        title_line = mod.__doc__.splitlines()[0] if mod.__doc__ else mod_name
        ok = run_cases(title_line, mod.cases)
        results.append((mod_name, ok))

    print(f"\n{BOLD}{'=' * 62}{RESET}")
    print(f"{BOLD}  შემაჯამებელი{RESET}")
    print(f"{BOLD}{'=' * 62}{RESET}")
    passed = sum(1 for _, ok in results if ok)
    for name, ok in results:
        mark = f"{GREEN}✓{RESET}" if ok else f"{RED}✗{RESET}"
        print(f"  {mark} {name}")
    total = len(results)
    color = GREEN if passed == total else YELLOW
    print(f"\n{color}{BOLD}სულ: {passed}/{total} სავარჯიშო წარმატებულია{RESET}\n")
    return 0 if passed == total else 1


if __name__ == "__main__":
    sys.exit(main())
