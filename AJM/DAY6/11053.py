#가장 긴 증가하는 부분 수열

"""
0  1  2  3  4  5
10 20 10 30 20 50

dp
1  1  1  1  1  1
1  2
1  2  1
1  2  1  3
"""
n = int(input())
arr = list(map(int,input().split()))

dp = [1]*n

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i],dp[j]+1)
    
print(max(dp))
