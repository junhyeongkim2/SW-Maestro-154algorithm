"""효율적인 화폐구성
DP 이코테 p.228
봐도 봐도 모르겠어 ㅠㅠ
"""

import sys
input = sys.stdin.readline

n, m = map(int,input().split())
arr = []
for i in range(n):
  arr.append(int(input()))

dp = [9999] * (m + 1)
dp[0] = 0 
for i in range(n):
    for j in range(arr[i], m+1):
        dp[j] = min(dp[j], dp[j - arr[i]] +1 )
        #현재 금액에서 
if dp[m] == 9999:
    print(-1)
else: 
    print(dp[m])
