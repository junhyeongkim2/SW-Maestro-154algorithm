import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n = int(input())
  
  dp = [[0]*100000,[0]*100000]
  
  for idx, var in enumerate(map(int,input().split())):
    dp[0][idx] = var
  for idx, var in enumerate(map(int,input().split())):
    dp[1][idx] = var
  
  dp[0][1] += dp[1][0]
  dp[1][1] += dp[0][0]
  
  # 맨 끝에서 시작 -> 둘 중 하나는 무조건 고르게 됨
  # ex - (1,위) 선택 => (0,아래) 선택됨
  # 2번 인덱스 부터는 선택지가 갈린다. 예를 들어 (2,위) 선택 시
  # (1) (1,아래)을 선택하면 (0,위)도 자동으로 선택된다.
  # (2) (0,아래) 선택
  # (1)과 (2) 중 큰 값을 선택한다.
  
  for i in range(2, n):
    dp[0][i] += max(dp[1][i-1], dp[1][i-2])
    dp[1][i] += max(dp[0][i-1], dp[0][i-2])
  
  print(max(dp[0][n-1], dp[1][n-1]))