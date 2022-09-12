def is_armstrong_number(number):
    """Determine if a number is an Armstrong number, a number that
    is the sum of its own digits each raised to the power of the number of digits.

    :param number: int - number to determine if is an Armstrong number
    :return bool: True if the number is an Armstrong number, False if it is not. 
    """
    digits = [int(n) for n in f"{number}"]
    n_digits = len(digits)

    return sum(n**n_digits for n in digits) == number

