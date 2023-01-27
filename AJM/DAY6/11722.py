#가장 긴 감소하는 부분 수열

n = int(input())
arr = list(map(int,input().split()))

dp = [1]*1000

for i in range(1,n):
    for j in range(i):
        if arr[i] < arr[j]:
            dp[i] = max(dp[i],dp[j]+1)
    
print(max(dp))
