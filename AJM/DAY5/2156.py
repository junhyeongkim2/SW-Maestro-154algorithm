#포도주 시식

"""
6   10      13      9         8           1
d1  d2      d3      d4        d5          d6
d1  d1+d2   d1+d3   d1+d2+d4  d1+d2+d4+d5
            d2+d3   d2+d3     d1+d3+d5
            d1+d2   d1+d3+d4  d2+d3+d5
    16      23      28        33          33
            d2+d3

dp[4] = max(dp[3],dp[3]+d[4],dp[2]+d[4])

규칙: dp[i-1],dp[i-3]+d[i-1]+d[i],dp[i-2]+d[i] 중에 가장 큰값이 dp[i]

"""
n = int(input())
arr = [0]
for i in range(n):
    arr.append(int(input()))
    
dp = [0]*10001
dp[1] = arr[1]
for i in range(2,n+1):
    if i<3:
        dp[i] = arr[i]+arr[i-1]
    else:
        dp[i] = max(dp[i-1],dp[i-3]+arr[i-1]+arr[i],dp[i-2]+arr[i])

print(dp[n])
