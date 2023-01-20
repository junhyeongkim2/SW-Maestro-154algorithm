import sys
input = sys.stdin.readline

n = int(input())
dp = [[0 for _ in range(10)] for j in range(101)]

#         0 1 2 3 4 5 6 7 8 9
# 1자리   0 1 1 1 1 1 1 1 1 1
# 2자리   1 1 2 2 2 2 2 2 2 1
# 3자리   1 3 3 4 4 4 4 4 3 2
# 4자리   3 3 7 7 8 8 8 7 6 3

# 1자리 초기화
for i in range(1,10):
  dp[1][i] = 1
  
for i in range(2, n+1): # 자리수 
  for j in range(10): # 0~9 - 각 숫자의 개수
    if j == 0:
      dp[i][j] = dp[i-1][j+1] # 오른쪽 대각선
    elif j == 9:
      dp[i][j] = dp[i-1][j-1] # 왼쪽 대각선
    else:
      dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1] # 오른쪽 + 왼쪽
result = 0
for i in range(10):
  result += dp[n][i]
  
print(result%1000000000)

