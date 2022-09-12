def divide_number(number):
    divs = {
        0: lambda number: number / 2,
        1: lambda number: 3 * number + 1,
    }
    
    return divs[number % 2](number) 

def steps(number):
    step = 0
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    while number != 1:
        number = divide_number(number)
        step += 1
    
    return step
