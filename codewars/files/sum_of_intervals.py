"""
https://www.codewars.com/kata/52b7ed099cdc285c300001cd
    Sum of Intervals
Write a function called sumIntervals/sum_intervals() that accepts an array of intervals, and returns the sum of all the interval lengths. Overlapping intervals should only be counted once.

Intervals
Intervals are represented by a pair of integers in the form of an array. The first value of the interval will always be less than the second value. Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.

Overlapping Intervals
List containing overlapping intervals:

[
   [1,4],
   [7, 10],
   [3, 5]
]
The sum of the lengths of these intervals is 7. Since [1, 4] and [3, 5] overlap, we can treat the interval as [1, 5], which has a length of 4.

Examples:
sumIntervals( [
   [1,2],
   [6, 10],
   [11, 15]
] ); // => 9

sumIntervals( [
   [1,4],
   [7, 10],
   [3, 5]
] ); // => 7

sumIntervals( [
   [1,5],
   [10, 20],
   [1, 6],
   [16, 19],
   [5, 11]
] ); // => 19

"""


def sum_of_intervals(intervals):
    def length(pair): return pair[1] - pair[0]

    intervs = sorted(intervals)
    print(intervs)

    len_ = sum([length(e) for e in intervs])
    diffs = [-(min(intervs[idx + 1]) - max(pair))
             for idx, pair in enumerate(intervs[:-1])]

    neg_diffs = [diff for diff in diffs if diff < 0]
    print(neg_diffs)

    return len_ + sum(neg_diffs)


def sum_of_intervals_v2(intervals):
    def length(pair): return pair[1] - pair[0]

    def overlap(pair_a, pair_b):
        a_max, a_min = max(pair_a), min(pair_a)
        b_max, b_min = max(pair_b), min(pair_b)

        if a_max > b_min:
            if a_max < b_max:
                return (a_min, b_max)
            else:
                return (a_min, a_max)
        else:
            return a_max > b_min

    if len(intervals) == 1:
        return length(intervals[0])

    new_intervs = sorted(intervals)
    interv_lengths = []

    for i, pair in enumerate(new_intervs[:-1]):
        check_overlap = overlap(new_intervs[i], new_intervs[i + 1])

        if check_overlap:
            new_intervs[i + 1] = check_overlap
            interv_lengths.append(check_overlap)
            # new_intervs.pop(i)
            # print(check_overlap)
            # print(interv_lengths)
        else:
            if new_intervs[i] not in interv_lengths:
                interv_lengths.append(new_intervs[i])
            if new_intervs[i + 1] not in interv_lengths:
                interv_lengths.append(new_intervs[i + 1])

    print(interv_lengths)

    #print(sum([length(e) for e in interv_lengths]))

    return sum([length(e) for e in interv_lengths])


def sum_of_intervals_v1(intervals):
    def length(pair): return pair[1] - pair[0]

    if len(intervals) == 1:
        return length(intervals[0])

    intervals = sorted(intervals)

    new_intervals = []
    for idx, pair in enumerate(intervals[:-1]):
        a, b = pair
        c, d = intervals[idx + 1]
        print(pair)
        print(intervals[idx + 1])
        print((c < b))

    pass


#print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]), 7)
