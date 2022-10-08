def color_code(color) -> int:
    """Look up the numerical value associated with a particular
    encoding color band.

    :param color: str - color to look up
    :return: int - numerical value associated with given color
    """
    return colors().index(color)


def colors() -> list:
    """List the encoding band colors.

    :return: list - list of different band colors
    """
    encoding = [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white",
    ]
    return encoding
