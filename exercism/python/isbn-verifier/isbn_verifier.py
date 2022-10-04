import re

def get_isbn_digits(isbn) -> str:
    """Filter characters 0 to 9 from the string.

    :param isbn: str - string to filter digits from.
    :return: str - string containing only digits (0 to 9).
    """
    isbn_digits = ''.join(num for num in re.split(r"(\d+)", isbn, flags=0) if num and num.isnumeric())
    return isbn_digits

def is_valid(isbn) -> bool:
    """Determine if the string passed correspond to a valid ISBN-10.
    The ISBN-10 formats is 9 digits (0 to 9) plus one check character (either a digit or an X only).
    In case the check character is an X, this represents the value '10'.
    These may be comunicated with or without hyphens, and can be checked for their validity by the
    following formula:
    (d₁ * 10 + d₂ * 9 + d₃ * 8 + d₄ * 7 + d₅ * 6 + d₆ * 5 + d₇ * 4 + d₈ * 3 + d₉ * 2 + d₁₀ * 1) mod 11 == 0
    If the result is 0, then it is a valid ISBN-10, otherwise it is invalid.

    :param isbn: str - string to determine if contains a valid ISBN-10.
    :return: bool - True if it contains a valid ISBN-10, False otherwise.
    """
    isbn = isbn.replace('-', '')
    isbn_len = (len(isbn) == 10)

    isbn_digits = get_isbn_digits(isbn)

    x_flag = isbn.endswith('X')
    isbn_check = x_flag or isbn.isdigit()

    if isbn_len and isbn_check:
        isbn_sum = sum([a * int(b) for a, b in zip(range(10, 0, -1), isbn_digits)])
        if x_flag:
            isbn_sum += 10
        return isbn_sum % 11 == 0

    return False