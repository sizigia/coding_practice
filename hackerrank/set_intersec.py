n = int(input())
s = set(map(int, input().split()))

b = int(input())
sb = set(map(int, input().split()))

print(len(s.intersection(sb)))


# Sample input:
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8
# Example:
# >> > s = set("Hacker")
# >> > print s.intersection("Rank")
# set(['a', 'k'])

# >> > print s.intersection(set(['R', 'a', 'n', 'k']))
# set(['a', 'k'])

# >> > print s.intersection(['R', 'a', 'n', 'k'])
# set(['a', 'k'])

# >> > print s.intersection(enumerate(['R', 'a', 'n', 'k']))
# set([])

# >> > print s.intersection({"Rank": 1})
# set([])

# >> > s & set("Rank")
# set(['a', 'k'])
