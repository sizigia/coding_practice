def value(colors) -> int:
    """Return value of dual resistor.

    :param colors: list - list of resistor colors
    :return: int - dual resistor value
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

    value_temp = "{}{}"
    value_colors = [encoding.index(color) for color in colors[:2]]

    return int(value_temp.format(*value_colors))
