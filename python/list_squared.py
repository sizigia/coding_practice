"""
https://www.codewars.com/kata/55aa075506463dac6600010d/train/python
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


def list_squared(m, n):
    import math
    primes = sieve(n, sliced=True, start=m, stop=n)
    list_sq = []

    for idx, num in enumerate(range(m, n)):
        if primes[idx]:
            sq_div = [1, num**2]
        else:
            sq_div = [
                int_**2 for int_ in list(range(1, num + 1)) if (num % int_ == 0)]

        sum_div = sum(sq_div)
        sq = math.sqrt(sum_div)
        if sq == int(sq):
            list_sq.append([num, sum_div])

    return list_sq


def sieve(n, sliced=None, start=None, stop=None):
    prime = [True] * n
    p = 1

    while (p * p <= n):
        for i in range(p * p, n, p):
            prime[i] = False
        p += 1
    if sliced:
        stop += 1
        return prime[start:stop]
    return prime
