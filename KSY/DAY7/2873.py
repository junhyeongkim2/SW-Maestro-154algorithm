import sys
input = sys.stdin.readline

# def beOdd(railBoard, odd, theOther):


r, c = map(int, input().split())
railBoard = [[0]*c for _ in range(r)]
for i in range(r):
    railBoard[i] = list(map(int, input().split()))

row, column, result = 0, 0, 0
#풀이1
# if c % 2 == 0: #열이 짝수
#     if r % 2 == 0: #행이 짝수
#         pass
#     else: #행이 홀수
#         while row != r-1 and column != c-1:
#             for _ in range(c):
#                 result += railBoard[row][column]
#                 column += 1
#             row += 1
#             for _ in range(c):
#                 result += railBoard[row][column]
#                 column -= 1
# else: #열이 홀수
#     if r % 2 == 0: #행이 짝수
#         pass
#     else: #행이 홀수
#         while row != r - 1 and column != c - 1:
#             for _ in range(c):
#                 result += railBoard[row][column]
#                 column += 1
#             row += 1
#             for _ in range(c):
#                 result += railBoard[row][column]
#                 column -= 1

if r % 2 == 1:
    print(("R"*(c-1) + "D" + "L"*(c-1) + "D")*(r//2) + "R"*(c-1))
elif c % 2 == 1:
    print(("D"*(r-1) + "R" + "U"*(r-1) + "R")*(c//2) + "D"*(r-1))
else: #*****
    position = [0, 0]
    removeNumbers = 1000
    for i in range(r):
        if i % 2 == 1:
            for j in range(1, c, 2):
                if railBoard[i][j] < removeNumbers:
                    position = [i, j]
                    removeNumbers = railBoard[i][j]
        else: # i % 2 == 0
            for j in range(c, 2):
                if railBoard[i][j] < removeNumbers:
                    position = [i, j]
                    removeNumbers = railBoard[i][j]

#온전히 풀지 못 함
