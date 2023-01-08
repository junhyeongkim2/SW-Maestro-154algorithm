# 2156번 포도주 시식
# https://www.acmicpc.net/problem/2156

# 계단 오르기 문제랑 헷갈리지 말자.
# 굳이 한 칸, 두 칸씩 띄어 안 마셔도 된다.
import sys
read = sys.stdin.readline

N = int(read().strip())
arr = [0]+[int(read().strip()) for _ in range(N)]
if N==1:
    print(arr[1])
    exit()
elif N==2:
    print(arr[1]+arr[2])
    exit()

# 각 인덱스에서의 값은 해당 위치에서의 최대 포도주 양을 의미
dp = [0, arr[1], arr[1]+arr[2], arr[3]+max(arr[1], arr[2])] 
for i in range(3, N+1):
    dp.append(max(arr[i-1]+max(dp[i-3], dp[i-4]), dp[i-2])+arr[i])

# dp = [0, arr[1], arr[1]+arr[2]]
# for i in range(3, N+1):
#     # dp.append(max(arr[i-1]+max(dp[i-3], dp[i-4]), dp[i-2])+arr[i])
#     dp.append(max(dp[i-1], max(dp[i-2], dp[i-3]+arr[i-1])+arr[i]))

print(max(dp))