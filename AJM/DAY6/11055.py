#가장 큰 증가 부분 수열


"""
0  1   2  3  4  5  6  7  8  9
10 100 2  50 60 3  5  6  7  8

dp
1 0   0
1 101
1 101 3
1 101 3 53

"""
n = int(input())
arr = list(map(int,input().split()))

dp = [0]*1000
dp[0] = arr[0]

for i in range(1,n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i],dp[j]+arr[i])
        else:
            dp[i] = max(dp[i],arr[i])
    
print(max(dp))
