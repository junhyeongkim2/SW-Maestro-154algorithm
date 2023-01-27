# 11052번 카드 구매하기
# https://www.acmicpc.net/problem/11052

N = int(input())
dp = [0]+list(map(int, input().split()))

for i in range(2,N+1):
    for j in range(i//2+1):
        dp[i] = max(dp[i], dp[j]+dp[i-j])
print(dp[N])