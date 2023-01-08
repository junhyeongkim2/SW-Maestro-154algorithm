# 9461번 파도반 수열
# https://www.acmicpc.net/problem/9461
import sys
read = sys.stdin.readline
T = int(read().strip())
arr = [int(read().strip()) for _ in range(T)]
M = max(arr)
dp = [1, 1, 1, 2, 2, 3, 4, 5]
for i in range(8, M+1):
    dp.append(dp[i-1]+dp[i-5])

for a in arr:
    print(dp[a-1])