n = int(input())
data = list(map(int, input().split()))

dp1 = [1]*n

# i로 끝나는 오름차순 순열 중 가장 긴 것
for i in range(n):
    for j in range(i):
        if data[i]>data[j]:
            dp1[i] = max(dp1[i], dp1[j]+1)

dp2 = [1]*n

# i로 시작하는 내림차순 순열 중 가장 긴 것
for i in range(n-1, -1, -1):
    for j in range(n-1, i-1, -1):
        if data[i]>data[j]:
            dp2[i] = max(dp2[i], dp2[j]+1)

dp = [0]*n
for i in range(n):
    dp[i] = dp1[i]+dp2[i]
print(max(dp)-1)