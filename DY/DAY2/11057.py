# 11057번 오르막 수
# https://www.acmicpc.net/problem/11057

N = int(input())
dp = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for _ in range(N-1):
    prev = dp[:]
    for j in range(10):
        dp[j] += sum(prev[0:j])
print(sum(dp)%10007)