n = int(input())
s = set(map(int, input().split()))

b = int(input())
sb = set(map(int, input().split()))

print(len(s.symmetric_difference(sb)))


# Example:
# >> > s = set("Hacker")
# >> > print s.symmetric_difference("Rank")
# set(['c', 'e', 'H', 'n', 'R', 'r'])

# >> > print s.symmetric_difference(set(['R', 'a', 'n', 'k']))
# set(['c', 'e', 'H', 'n', 'R', 'r'])

# >> > print s.symmetric_difference(['R', 'a', 'n', 'k'])
# set(['c', 'e', 'H', 'n', 'R', 'r'])

# >> > print s.symmetric_difference(enumerate(['R', 'a', 'n', 'k']))
# set(['a', 'c', 'e', 'H', (0, 'R'), 'r', (2, 'n'), 'k', (1, 'a'), (3, 'k')])

# >> > print s.symmetric_difference({"Rank": 1})
# set(['a', 'c', 'e', 'H', 'k', 'Rank', 'r'])

# >> > s ^ set("Rank")
# set(['c', 'e', 'H', 'n', 'R', 'r'])
