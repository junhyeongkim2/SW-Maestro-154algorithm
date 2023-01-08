# 11055번 가장 큰 증가 부분 수열
# https://www.acmicpc.net/problem/11055

N = int(input())
arr = list(map(int, input().split()))
dp = [0]*N
for i in range(N):
    dp[i] = arr[i]
    for j in range(i):
        if arr[j]<arr[i]:
            dp[i] = max(dp[i], dp[j]+arr[i])
print(max(dp))