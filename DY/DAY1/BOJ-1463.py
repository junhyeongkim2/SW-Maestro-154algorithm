# 1463번 1로 만들기
# https://www.acmicpc.net/problem/1463

import sys
input = sys.stdin.readline

N = int(input())
dp = [0]*(N+1) # 횟수 저장할 list

for i in range(2,N+1):
    dp[i] = dp[i-1] + 1 # +1 은 횟수가 1회 증가함을 의미
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)

print(dp[N])