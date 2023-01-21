import sys
input = sys.stdin.readline
N = int(input())
num = [0] * 10001

for i in range(N):
    num[int(input())] += 1

for i in range(10001):
    if not num[i] == 0:
        for j in range(num[i]):
            print(i)