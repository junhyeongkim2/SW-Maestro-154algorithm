#이친수

"""
자리수 1 : 1
자리수 2 : 10
자리수 3 : 101 100
자리수 4 : 1010 1000 1001
자리수 5 : 10101 10100 10001 10000 10010
자리수 6 : 101010 101000 101001 100010 100101 100100

자리수 n-1 뒤에 0을 붙임 (기존 개수 유지)
추가되는거는 1을 붙일수있냐업냐


"""

n = int(input())

dp = [0]*91
dp[1] = 1
dp[2] = 1

for i in range(3,n+1):
    dp[i] = dp[i-1]+dp[i-2]
print(dp[n])
