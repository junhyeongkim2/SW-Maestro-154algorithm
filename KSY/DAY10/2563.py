import sys
input = sys.stdin.readline
n = int(input())
result = 0
paper = [[0]*100 for _ in range(100)] #100x100 도화지

for _ in range(n):
    x, y = map(int, input().split()) #(x, y) 위치의 색종이

    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1

for r in paper:
    result += r.count(1)

print(result)