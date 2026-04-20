"""
სავარჯიშო 6: სტუდენტების ანალიზი
==================================

მოცემული გაქვთ სტუდენტების list dictionary-ების სახით:
    [{"name": "ანა", "score": 75}, {"name": "ნიკა", "score": 92}, ...]

დაწერეთ ფუნქცია `analyze_students(students)`, რომელიც ამ list-ს მიიღებს და
დააბრუნებს dictionary-ს, რომელიც შეიცავს:
    - "average":  საშუალო ქულა (float)
    - "top":      ყველაზე მაღალქულიანი სტუდენტის სახელი (str)
    - "failed":   ჩაჭრილ სტუდენტთა (ქულა < 50) სახელების სია (list[str])

მაგალითი:
    >>> students = [
    ...     {"name": "ანა",  "score": 75},
    ...     {"name": "ნიკა", "score": 92},
    ...     {"name": "გიო",  "score": 45},
    ... ]
    >>> analyze_students(students)
    {'average': 70.67, 'top': 'ნიკა', 'failed': ['გიო']}

ტესტის გასაშვებად:
    python tests/test_exercise_06.py
"""


def analyze_students(students: list[dict]) -> dict:
    # 👇 შენი კოდი აქ
    raise NotImplementedError("წაშალე ეს ხაზი და ჩაწერე შენი კოდი")


if __name__ == "__main__":
    sample = [
        {"name": "ანა",  "score": 75},
        {"name": "ნიკა", "score": 92},
        {"name": "გიო",  "score": 45},
        {"name": "მარი", "score": 38},
        {"name": "ლუკა", "score": 72},
    ]
    print(analyze_students(sample))
