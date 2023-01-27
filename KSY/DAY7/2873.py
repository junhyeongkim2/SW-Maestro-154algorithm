import sys
input = sys.stdin.readline

# def beOdd(railBoard, odd, theOther):


r, c = map(int, input().split())
railBoard = [[0]*c for _ in range(r)]
for i in range(r):
    railBoard[i] = list(map(int, input().split()))

row, column, result = 0, 0, 0

if c % 2 == 0: #열이 짝수
    if r % 2 == 0: #행이 짝수
        pass
    else: #행이 홀수
        while row != r-1 and column != c-1:
            for _ in range(c):
                result += railBoard[row][column]
                column += 1
            row += 1
            for _ in range(c):
                result += railBoard[row][column]
                column -= 1
else: #열이 홀수
    if r % 2 == 0: #행이 짝수
        pass
    else: #행이 홀수
        while row != r - 1 and column != c - 1:
            for _ in range(c):
                result += railBoard[row][column]
                column += 1
            row += 1
            for _ in range(c):
                result += railBoard[row][column]
                column -= 1


print(result)