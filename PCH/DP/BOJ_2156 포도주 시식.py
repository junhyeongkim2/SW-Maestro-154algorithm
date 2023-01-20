import sys
input = sys.stdin.readline
n = int(input())
w = [0]
for i in range(n):
  w.append(int(input()))

dp = [0]
dp.append(w[1])
if n > 1:
  dp.append(w[1]+w[2])
  for i in range(3, n+1):
    #         xox      xoo                      oxo
    dp.append(max(dp[i-1], w[i] + w[i-1] + dp[i-3], dp[i-2] + w[i]))

# dp[4]의 경우의 수를 보면 w2 + w3은 dp[3]이고, w1 + w2 + w4에서 w1 + w2는 dp[2]이다.
# 그리고 w1 + w3 + w4에서 w1은 dp[1]이다. 그래서 식을 세워보자면,
# dp[4]의 경우의 수 : dp[4 - 1], dp[4 - 3] + w[4 - 1] + w[4], dp[4 - 2] + w[4]
# 4를 i로 바꿨을때
# dp[i - 1], dp[i - 3] + w[i - 1] + w[i], dp[i - 2] + w[i] 이 세가지 값중 가장 큰 값을 넣어주면 된다.

print(dp[n])