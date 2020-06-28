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

    for _ in range(start, end + 1):
        if _ % 3 == 0:
            s += 'Fizz'

        if _ % 5 == 0:
            s += 'Buzz'

        if len(s) == 0:
            s = _

        if _ == 100:
            return s

        print(s)
        s = ""


if __name__ == "__main__":
    fizzbuzz(8, 16)
