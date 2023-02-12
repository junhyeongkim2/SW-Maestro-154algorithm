'''
게임 개발
'''

# Input
n, m = map(int, input().split())
x, y, direction = map(int, input().split())
map_arr = [list(map(int, input().split())) for _ in range(n)]

# Define variables
checked = [[0]*m]*n
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
count = 1

# Define functions
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
    
# Algorithm
while True:
    move = False
    for i in range(4):
        turn_left()
        tmp_x = x + dx[direction]
        tmp_y = y + dy[direction]
        if map_arr[tmp_x][tmp_y] == 0 and checked[tmp_x][tmp_y] == 0:
            x, y = tmp_x, tmp_y
            checked[x][y] = 1
            count += 1
            move = True
            break
    if move == False:
        tmp_x = x - dx[direction]
        tmp_y = y - dy[direction]
        if map_arr[tmp_x][tmp_y] == 0:
            x, y = tmp_x, tmp_y
        else:
            break
         
# Output
print(count)
