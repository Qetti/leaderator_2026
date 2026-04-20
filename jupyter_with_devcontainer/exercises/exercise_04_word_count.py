"""
სავარჯიშო 4: სიტყვების დათვლა
==============================

დაწერეთ ფუნქცია `word_count(text)`, რომელიც ტექსტში ყოველი სიტყვის
გამეორების რაოდენობას დააბრუნებს dictionary-ის სახით.

მაგალითი:
    >>> word_count("hello world hello python")
    {'hello': 2, 'world': 1, 'python': 1}

    >>> word_count("apple banana apple apple banana")
    {'apple': 3, 'banana': 2}

ტესტის გასაშვებად:
    python tests/test_exercise_04.py
"""


def word_count(text: str) -> dict[str, int]:
    # 👇 შენი კოდი აქ
    raise NotImplementedError("წაშალე ეს ხაზი და ჩაწერე შენი კოდი")


if __name__ == "__main__":
    print(word_count("hello world hello python"))
