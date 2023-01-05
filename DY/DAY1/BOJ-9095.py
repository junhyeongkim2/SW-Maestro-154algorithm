# 9095번 1,2,3 더하기
# https://www.acmicpc.net/problem/9095

T = int(input())
nums = [int(input()) for _ in range(T)]

dp = [0, 1, 2, 4]
for i in range(4, max(nums)+1):
    dp.append(dp[i-1]+dp[i-2]+dp[i-3])

for n in nums:
    print(dp[n])