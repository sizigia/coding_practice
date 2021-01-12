"""
https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes/problem
Integers in Python can be as big as the bytes in your machine's memory. 
There is no limit in size as there is: 2^31 - 1 (C++ int) or 2^63 - 1 (C++ long long int).

As we know, the result of a^b grows really fast with increasing b.

Let's do some calculations on very large integers.

# Task 
Read four numbers, a, b, c, and d, and print the result of a^b + c^d.

# Input Format 
Integers a, b, c, and d are given on four separate lines, respectively.

# Constraints
1 <= a <= 1000
1 <= b <= 1000
1 <= c <= 1000
1 <= d <= 1000

Output Format 
Print the result of a^b + c^d on one line.
"""
a, b, c, d = (int(input()) for _ in range(4))

if __name__ == '__main__':
    res = a ** b + c ** d
    assert (a**b + c**d) == 4710194409608608369201743232
