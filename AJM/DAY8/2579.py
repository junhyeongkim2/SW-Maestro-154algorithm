#2579 계단 오르기
n = int(input())
arr = [0]*301
dp = [0]*301
for i in range(n):
    arr[i] = int(input())

"""
마지막 계단 x-1 계단을 밟으면 x-2는 밟으면 안됨.
x-2를 밟으면 그 전꺼는 상관없음.
10 20 15 25 10 20
"""

dp[0] = arr[0]
dp[1] = arr[0]+arr[1]
dp[2] = max(arr[0]+arr[2],arr[1]+arr[2])

for i in range(3,n):
    dp[i]= max(dp[i-3]+arr[i-1]+arr[i],dp[i-2]+arr[i])

print(dp[n-1])
