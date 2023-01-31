import sys
input = sys.stdin.readline

# 계수정렬 활용
n = int(input())
arr = [0] * (10000 + 1)

for _ in range(n):
    arr[int(input())] += 1

for i in range(len(arr)):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)
