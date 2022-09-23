def convert(number):
    """Convert a number to a string that contains raindrop sounds
    corresponding to potential factors.

    The rules of raindrops are that if a given number:
    - has 3 as a factor, add 'Pling' to the result.
    - has 5 as a factor, add 'Plang' to the result.
    - has 7 as a factor, add 'Plong' to the result.
    - does not have any of 3, 5, or 7 as a factor,
    the result should be the digits of the number.

    :param number: int - number to convert to string
    :return: str - string containing raindrops according to factors of input number.
    """

    factors = {
        'A': lambda number: "Pling" if number % 3 == 0 else "",
        'B': lambda number: "Plang" if number % 5 == 0 else "",
        'C': lambda number: "Plong" if number % 7 == 0 else "",
    }

    return f"{factors['A'](number)}{factors['B'](number)}{factors['C'](number)}" or f"{number}"
