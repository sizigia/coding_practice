def divide_number(number):
    divs = {
        0: lambda number: number / 2,
        1: lambda number: 3 * number + 1,
    }
    
    return divs[number % 2](number) 

def steps(number):
    """Determine the number of steps that take to reduce a given number to 1 by diving it by 2 if even; or multiplying it by 3 and adding 1, if odd. 

    :param number: int - number to be reduce to 1
    :return step: int - represents the number of steps required to reduce number to 1 
    """
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    step = 0
    while number != 1:
        number = divide_number(number)
        step += 1
    
    return step
