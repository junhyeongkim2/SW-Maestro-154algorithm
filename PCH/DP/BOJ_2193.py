import sys
input = sys.stdin.readline

n = int(input())

# 1
# 10
# 100 101
# 1000 1001 1010 
# 10000 10100 10010 10001 10101
# 100000 101000 100100 100010 100001 101010 101001 100101

dp = [0 for _ in range(n)]
dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, n):
  dp[i] = dp[i-1] + dp[i-2]
  
print(dp[n-1])