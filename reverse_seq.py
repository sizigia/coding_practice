"""
https://www.codewars.com/kata/5a00e05cc374cb34d100000d/train/python

Get the number n (n>0) to return the reversed sequence from n to 1.

Example : n=5 >> [5,4,3,2,1]
"""


def reverse_seq(n):
    seq_ = list(range(1, n + 1))

    return list(reversed(seq_))
