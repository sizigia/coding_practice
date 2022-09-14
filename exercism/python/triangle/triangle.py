def is_triangle(sides):
    positive_lengths = all(side > 0 for side in sides)

    inequalities = {
        'first': sides[0] + sides[1] >= sides[2],
        'second': sides[1] + sides[2] >= sides[0],
        'third': sides[0] + sides[2] >= sides[1]
    
    }
    
    return positive_lengths and all(test for test in inequalities.values())

def equilateral(sides):
    """Determine if a triangle is equilateral, it has all three sides of same length.

    :param sides: list - sequence of side lengths
    :return: bool - True if the triangle is equilateral, False if not.
    """
    
    return is_triangle(sides) and (sides.count(sides[0]) == len(sides))


def isosceles(sides):
    """Determine if a triangle is isosceles, it has two sides the same length.

    :param sides: list - sequence of side lengths
    :return: bool - True if the triangle is isosceles, False if not.
    """
    
    return is_triangle(sides) and (sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2])


def scalene(sides):
    """Determine if a triangle is scalene, it has all sides of different lengths.

    :param sides: list - sequence of side lengths
    :return: bool - True if the triangle is scalene, False if not.
    """
    
    return is_triangle(sides) and (len(set(sides)) == 3)
