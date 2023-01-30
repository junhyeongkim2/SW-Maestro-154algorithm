import sys
input = sys.stdin.readline

n = int(input())
list = []

for i in range(n):
    x, y = map(int, input().split())
    list.append([x, y])


for i in list:
    print(i[0], i[1])
