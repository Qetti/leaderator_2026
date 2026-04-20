"""
სავარჯიშო 1: მისალმება
=======================

დაწერეთ ფუნქცია `greet(name, age)`, რომელიც აბრუნებს სტრიქონს ფორმატში:

    "გამარჯობა, [სახელი]! [X] წლის შემდეგ 100 წლის გახდები."

სადაც X = 100 - age.

მაგალითი:
    >>> greet("ანა", 25)
    'გამარჯობა, ანა! 75 წლის შემდეგ 100 წლის გახდები.'

ტესტის გასაშვებად:
    python tests/test_exercise_01.py
"""


def greet(name: str, age: int) -> str:
    # 👇 შენი კოდი აქ
    raise NotImplementedError("წაშალე ეს ხაზი და ჩაწერე შენი კოდი")


if __name__ == "__main__":
    # ცოცხალი ტესტი — ინტერაქტიული input-ით
    user_name = input("სახელი: ")
    user_age = int(input("ასაკი: "))
    print(greet(user_name, user_age))
