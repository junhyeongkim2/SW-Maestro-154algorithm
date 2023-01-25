#연속 합

"""
그 전꺼랑 더해서 작다고 아예 안더하는게 아니라
일단 그냥 arr에 있는거보다 더한게 크면 일단 저장

10
2 1 -4 3 4 -4 6 5 -5 1
2, 3, -1, 3, 7, 3, 9, 14, 9, 10
14
 

"""
n = int(input())

arr = list(map(int,input().split()))

dp = [arr[0]]

for i in range(n-1):
    dp.append(max(dp[i]+arr[i+1],arr[i+1]))

print(max(dp))
