"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(n_layers):
    """Calculate the time of preparation for the lasagna,
    depending on the number of layers you want to add to it.

    :param n_layers: int - number of layers to add to the lasagna.
    :return: int - preparation time (in minutes) derived from 'PREPARATION_TIME'.

    Function that takes the number of layers you want to add to the lasagna as
    an argument and returns how many minutes you would spend making it,
    based on the 'PREPARATION_TIME'.
    """

    return n_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed cooking time (preparation and baking)
    in minutes.

    :param number_of_layers: int - number of layers added to the lasagna
    :param elapsed_bake_time: int - number of minutes the lasagna has been baking in the oven
    :return: int - total number of minutes you've been cooking

    Function that returns the total number of minutes you've been cooking,
    or the sum of your preparation time and the time
    the lasagna has already spent baking in the oven.
    """

    prep_time = preparation_time_in_minutes(number_of_layers)

    return prep_time + elapsed_bake_time
