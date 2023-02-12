'''
왕실의 나이트
'''

# Input
position = input()

# Define variables
count = 0
move = [(2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)]
x = ord(position[0]) - ord('a') + 1
y = int(position[1])

# Algorithm
for dx, dy in move:
    if 1 <= x + dx <= 8 and 1 <= y + dy <= 8:
        count += 1

# Output
print(count)