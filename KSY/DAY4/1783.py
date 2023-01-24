n, m = map(int, input().split())
# board = [[0]*n for _ in range(m)]
# a, b, c, d = 0, 0, 0, 0
# x, y = 0, 0
#
# while a != 1 and b != 1 and c != 1 and d != 1:
#     if x + 2 < m and y + 1 < n and a != 1 and board[x+2][y+1] != 0: #오른2 아래1
#         board[x+2][y+1] = 1
#         a = 1
#     elif x + 1 < m and y + 2 < n and b != 1 and board[x+1][y+2] != 0: #오른1 아래2
#         board[x+1][y+2] = 1
#         b = 1
#     elif x + 2 < m and y - 1 < n and c != 1 and board[x+2][y-1] != 0: #오른2 위1
#         board[x+2][y-1] = 1
#         c = 1
#     elif x + 1 < m and y - 2 < n and d != 1 and board[x+1][y-2] != 0: #오른2 위1
#         board[x+1][y-2] = 1
#         d = 1
# else:
#     print(board.count(1))


if n == 1:
    print(1)
elif n == 2:
    print(min(4, (m-1)//2 + 1))
elif m <= 6:
    print(min(4, m))
else:
    print(m-2)