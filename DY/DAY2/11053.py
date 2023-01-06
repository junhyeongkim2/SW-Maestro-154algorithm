# 11053번 가장 긴 증가하는 부분 수열
# https://www.acmicpc.net/problem/11053

N = int(input())
arr = list(map(int, input().split()))
dp = [1]*N
for i in range(N):
    for j in range(i):
        if arr[j]<arr[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))