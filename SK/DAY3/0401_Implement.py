'''
상하좌우
'''

# Input
n = int(input())
move_str = input().split()

# Define variables
x, y = 1, 1
direction = {
    'L' : (0, -1),
    'R' : (0, 1),
    'U' : (-1, 0),
    'D' : (1, 0)
    }

# Algorithm
for move in move_str:
    dx, dy = direction[move]
    if 1 <= x + dx <= n and 1 <= y + dy <= n:
        x += dx
        y += dy

# Output
print(x, y)