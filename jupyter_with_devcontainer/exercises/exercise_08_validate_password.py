"""
სავარჯიშო 8: პაროლის ვალიდაცია
================================

დაწერეთ ფუნქცია `validate_password(pwd)`, რომელიც შეამოწმებს პაროლს
4 წესის მიხედვით და დააბრუნებს list-ს იმ წესების სახელებით, რომლებიც
**არღვევენ** მოთხოვნას. თუ პაროლი ყველა წესს აკმაყოფილებს — აბრუნებს
ცარიელ list-ს.

წესები და შესაბამისი error-სახელები:
    - "too_short"     — პაროლი 8 სიმბოლოზე მოკლეა
    - "no_uppercase"  — არ არის არცერთი დიდი ასო (A-Z)
    - "no_digit"      — არ არის არცერთი ციფრი (0-9)
    - "no_special"    — არ არის არცერთი სპეცსიმბოლო
                        (!@#$%^&*()-_=+[]{};:,.<>?/\\|~`'")

მაგალითი:
    >>> validate_password("abc")
    ['too_short', 'no_uppercase', 'no_digit', 'no_special']

    >>> validate_password("Password1!")
    []

    >>> validate_password("password1!")
    ['no_uppercase']

    >>> validate_password("Short1!")
    ['too_short']

ტესტის გასაშვებად:
    python tests/test_exercise_08.py
"""


def validate_password(pwd: str) -> list[str]:
    # 👇 შენი კოდი აქ
    raise NotImplementedError("წაშალე ეს ხაზი და ჩაწერე შენი კოდი")


if __name__ == "__main__":
    print(validate_password("abc"))
    print(validate_password("Password1!"))
