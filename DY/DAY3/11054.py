# 11054번 가장 큰 증가 부분 수열
# https://www.acmicpc.net/problem/11054

N = int(input())
arr = list(map(int, input().split()))
dp = [1]*N # 감소 수열

for i in range(N-1,-1,-1):
    for j in range(N-1,i,-1):
        if arr[i]>arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))