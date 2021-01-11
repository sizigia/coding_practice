"""
https://www.codewars.com/kata/54e6533c92449cc251001667

Implement the function unique_in_order which takes as 
argument a sequence and returns a list of items without 
any elements with the same value next to each other and 
preserving the original order of elements.

For example:
    unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
    unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
    unique_in_order([1,2,2,3,3])       == [1,2,3]
"""


def unique_in_order(iterable):
    new_list = []

    for i in range(len(iterable)):
        a = iterable[i]
        if (i + 1) == len(iterable):
            new_list.append(iterable[-1])
            break
        else:
            b = iterable[i + 1]
        if a != b:
            new_list.append(a)

    return new_list
