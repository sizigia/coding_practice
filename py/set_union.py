n = int(input())
s = set(map(int, input().split()))


n2 = int(input())
s2 = set(map(int, input().split()))


print(len(s.union(s2)))


# Sample input:
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8


# Example:
# >> > s = set("Hacker")
# >> > print s.union("Rank")
# set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

# >> > print s.union(set(['R', 'a', 'n', 'k']))
# set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

# >> > print s.union(['R', 'a', 'n', 'k'])
# set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

# >> > print s.union(enumerate(['R', 'a', 'n', 'k']))
# set(['a', 'c', 'r', 'e', (1, 'a'), (2, 'n'), 'H', 'k', (3, 'k'), (0, 'R')])

# >> > print s.union({"Rank": 1})
# set(['a', 'c', 'r', 'e', 'H', 'k', 'Rank'])

# >> > s | set("Rank")
# set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])
