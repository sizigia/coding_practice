import math

def find_divisors(number):
    """Determine the positive factors of a number, not including the number itself.

    :param number: int - a positive integer
    :return: list - the positive factors of the input integer
    """
    divisors = [1]

    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            divisors.extend([i, number/i])

    return list(set(divisors))


def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    elif number == 1:
        return 'deficient'

    divisors = find_divisors(number)
    aliquot_sum = sum(divisors)

    classification = {
        'P': lambda number: 'perfect' if aliquot_sum == number else classification['A'](number),
        'A': lambda number: 'abundant' if aliquot_sum > number else classification['D'],
        'D': 'deficient'
    }

    return classification['P'](number)