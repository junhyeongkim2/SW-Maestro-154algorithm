# 11047번 동전 0
# https://www.acmicpc.net/problem/11047
# 23.01.13
import sys
read = sys.stdin.readline

N,K = map(int, read().split())
coin = [int(read().strip()) for _ in range(N)]

cnt = 0
for c in coin[::-1]:
    cur = K // c
    cnt += cur
    K -= c * cur
print(cnt)