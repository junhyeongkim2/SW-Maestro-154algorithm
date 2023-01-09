# 1912번 연속합
# https://www.acmicpc.net/problem/1912

N = int(input())
nums = list(map(int, input().split()))
for i in range(1, N):
    nums[i] = max(nums[i], nums[i]+nums[i-1])
print(max(nums))