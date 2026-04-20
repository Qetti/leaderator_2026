"""მარტივი ტესტ-რანერი სავარჯიშოებისთვის.

თითოეული ტესტი იძახებს `run_cases(title, cases)` ფუნქციას, სადაც cases არის
სიის სახით [(აღწერა, callable, მოლოდინი_ან_შემოწმების_ფუნქცია), ...].
"""

from __future__ import annotations

from typing import Any, Callable

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
DIM = "\033[2m"
RESET = "\033[0m"


def run_cases(title: str, cases: list[tuple[str, Callable[[], Any], Any]]) -> bool:
    """რანერი. აბრუნებს True-ს, თუ ყველა ქეისი წარმატებულია."""
    bar = "=" * 62
    print(f"\n{BOLD}{bar}{RESET}")
    print(f"{BOLD}  {title}{RESET}")
    print(f"{BOLD}{bar}{RESET}")

    passed = 0
    total = len(cases)

    for idx, (desc, fn, expected) in enumerate(cases, 1):
        label = f"ქეისი {idx}: {desc}"
        try:
            actual = fn()
        except NotImplementedError:
            print(f"  {YELLOW}⋯{RESET}  {label}")
            print(f"      {DIM}ამოცანა ჯერ არ არის გადაწყვეტილი (NotImplementedError){RESET}")
            continue
        except Exception as exc:  # noqa: BLE001
            print(f"  {RED}✗{RESET}  {label}")
            print(f"      {RED}შეცდომა:{RESET} {type(exc).__name__}: {exc}")
            continue

        if callable(expected):
            ok, msg = expected(actual)
            if ok:
                print(f"  {GREEN}✓{RESET}  {label}")
                passed += 1
            else:
                print(f"  {RED}✗{RESET}  {label}")
                print(f"      {msg}")
                print(f"      {DIM}მიღებული: {actual!r}{RESET}")
        elif actual == expected:
            print(f"  {GREEN}✓{RESET}  {label}")
            passed += 1
        else:
            print(f"  {RED}✗{RESET}  {label}")
            print(f"      {DIM}მოლოდინი:{RESET} {expected!r}")
            print(f"      {DIM}მიღებული:{RESET} {actual!r}")

    print()
    if passed == total:
        print(f"{GREEN}{BOLD}✓ წარმატება! ყველა ქეისი გავიდა ({passed}/{total}){RESET}\n")
        return True
    print(f"{YELLOW}{BOLD}შედეგი: {passed}/{total} ქეისი გავიდა — შეასწორე შეცდომები{RESET}\n")
    return False
