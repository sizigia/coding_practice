n = int(input())
s = set(map(int, input().split()))

b = int(input())
sb = set(map(int, input().split()))


print(len(s.difference(sb)))


# Sample input:
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8

# Example:
# >> > s = set("Hacker")
# >> > print s.difference("Rank")
# set(['c', 'r', 'e', 'H'])

# >> > print s.difference(set(['R', 'a', 'n', 'k']))
# set(['c', 'r', 'e', 'H'])

# >> > print s.difference(['R', 'a', 'n', 'k'])
# set(['c', 'r', 'e', 'H'])

# >> > print s.difference(enumerate(['R', 'a', 'n', 'k']))
# set(['a', 'c', 'r', 'e', 'H', 'k'])

# >> > print s.difference({"Rank": 1})
# set(['a', 'c', 'e', 'H', 'k', 'r'])

# >> > s - set("Rank")
# set(['H', 'c', 'r', 'e'])
