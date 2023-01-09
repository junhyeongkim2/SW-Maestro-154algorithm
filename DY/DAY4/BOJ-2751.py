import sys
input = sys.stdin.readline
N = int(input())

num = list(int(input()) for _ in range(N))
num.sort()
for i in range(len(num)):
    print(num[i])