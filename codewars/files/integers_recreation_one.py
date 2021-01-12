"""
https://www.codewars.com/kata/55aa075506463dac6600010d
Divisors of 42 are : 1, 2, 3, 6, 7, 14, 21, 42.
These divisors squared are: 1, 4, 9, 36, 49, 196, 441, 1764.
The sum of the squared divisors is 2500 which is 50 * 50, a square!

Given two integers m, n (1 <= m <= n) we want to find all integers between m and n whose sum of squared divisors is itself a square.
42 is such a number.

The result will be an array of arrays or of tuples or a string,
each subarray having two elements, first the number whose squared divisors is a square and then the sum of the squared divisors.

# Examples:

list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
list_squared(42, 250) --> [[42, 2500], [246, 84100]]

"""


from math import sqrt


def list_squared(m, n):
    import math
    from itertools import compress

    primes = sieve(n)
    list_sq = []

    for idx, num in enumerate(range(m, n)):
        if primes[idx]:
            sum_div = (1 + num**2) ** (1/2)
        else:
            sq_div = [
                int_**2 for int_ in range(1, num + 1) if (num % int_ == 0)]
            sum_div = sum(sq_div)

        sq = sum_div ** (1/2)
        if sq == int(sq):
            list_sq.append([num, sum_div])

    return list_sq


def sieve(n):
    """
    Calculate all the prime numbers between 2 and the given number n.
    Returns a list of booleans, where[1, ..., n] has been translated to:
        - True == is prime
        - False == not prime
    """
    prime = [True] * (n + 1)

    for p in range(2, int(n ** 0.5 + 1)):
        for i in range(p * p, n + 1, p):
            prime[i] = False

    return [idx for idx, p in enumerate(prime) if p]


if __name__ == '__main__':
    from itertools import compress
    import cProfile
    # cProfile.run('list_squared(42, 250)')
    cProfile.run('sieve(2500000)')

    """
    import math

    n = 42
    primes_42 = sieve(n)
    comp_list = compress(range(1, n + 1), primes_42)

    print("Prime numbers between 1 and 42:\n", list(comp_list))

    print("Divisors of 42:\n",
          [x for x in range(1, 43) if 42 % x == 0])

    print("Square of divisors of 42:\n",
          [x**2 for x in range(1, 43) if 42 % x == 0])

    print("Sum of square divisors of 42:\n",
          sum([x**2 for x in range(1, 43) if 42 % x == 0]))

    print("Square root of sum:\n",
          math.sqrt(sum([x**2 for x in range(1, 43) if 42 % x == 0])))

    print("Is the square root a square?\n",
          math.sqrt(sum([x**2 for x in range(1, 43) if 42 % x == 0])) == int(math.sqrt(sum([
              x**2 for x in range(1, 43) if 42 % x == 0]))))

    print("Prime numbers divisors of 42:\n",
          sum(map(lambda y: y**2 + 1, compress([x for x in range(1, 43) if 42 % x == 0], primes_42))))

    print("Odd numbers divisors of 42:\n",
          list(compress([x for x in range(1, 43) if 42 % x == 0], [not i for i in primes_42])))
    """
