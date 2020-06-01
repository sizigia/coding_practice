"""
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format
- The first line contains n. 
- The second line contains an array A[] of n integers each separated by a space.

Constraints:
2 <= n <= 10
-100 <= A[i] <= 100

Output Format: Print the runner-up score.
"""
import sys


def score_runner_up(n, arr, file=sys.stdout):
    _ = n
    list_ = list(arr)

    set_ = set(list_)
    set_.remove(max(list_))

    print(max(list(set_)), file=file)


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    score_runner_up(n, arr)
