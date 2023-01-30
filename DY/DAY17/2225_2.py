# 2225번 합분해
# https://www.acmicpc.net/problem/2225

# 1에서는 이전 칸에서의 모든 경우를 더해줬는데 그럴 필요가 없었다.
# 왜냐면 동일한 칸에서 이전 수가 앞의 경우를 모두 합산해서 가지고 있기 때문이다.

N, K = map(int, input().split())
dp = [[1]*(K+1)] + [[0]*(K+1) for _ in range(N)]
for num in range(1, N+1):
    for space in range(1, K+1):
        if space == 1: dp[num][space] = 1
        else:
            dp[num][space] = dp[num-1][space] + dp[num][space-1]
            dp[num][space] %= 1000000000
print(dp[N][K])