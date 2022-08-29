"""
Write a program that prints the numbers from 1 to 100. 
But for multiples of three print “Fizz” instead of the number and
 for the multiples of five print “Buzz”. 
For numbers which are multiples of both three and five print “FizzBuzz”.
"""


def fizzbuzz(start=1, end=101):
    """
    Multiple of 3, 5, or both.

    Prints out the next
    """

    s = ""
    end += 1

    for i in range(start, end):
        if i % 15 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)


if __name__ == "__main__":
    fizzbuzz(8, 17)
