# 10844 쉬운 계단 수
# https://www.acmicpc.net/problem/10844

N = int(input())
dp = [0]+[1]*9
for _ in range(N-1):
    prev = dp[:] # 이전 dp 복사
    dp[0] = prev[1]
    for i in range(1, 9):
        dp[i] = prev[i-1]+prev[i+1]
    dp[9] = prev[8]
print(sum(dp)%1000000000)

