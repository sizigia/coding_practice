def square_of_sum(number):
    """Calculate the square of the sum of the first N natural numbers.

    :param number: int - natural number N
    :return: int - square of the sum of [1; N]
    """
    
    return sum(range(1, number + 1))**2


def sum_of_squares(number):
    """Calculate the sum of th squares of the first N natural numbers.

    :param number: int - natural number N
    :return: int - sum of [1^2; N^2]
    """

    return (number * (number + 1) / 2) * (2 * number + 1) / 3


def difference_of_squares(number):
    """Calculate the different between the square of the sum and the sum of the squares of the first N natural numbers.

    :param number: int - natural number N
    :return: int - different between the square of sum of [1; N] and the sum of [1^2; N^2]
    """
    square_sum = square_of_sum(number)
    sum_squares = sum_of_squares(number)

    return square_sum - sum_squares
