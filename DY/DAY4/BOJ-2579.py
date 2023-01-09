# 2579번 계단 오르기
# https://www.acmicpc.net/problem/2579

# 2차원 배열을 사용한 풀이 방법
import sys
read = sys.stdin.readline

N = int(read().strip())
stair = [0]+[int(read().strip()) for _ in range(N)]
dp = [[0,0,0] for _ in range(N+1)]
# 첫 번째는 현재 계단의 인덱스, 두 번째는 몇 칸 연속 올라왔는지에 대한 인덱스

if N==1:
    print(stair[1])
    exit()
dp[1][1] = stair[1]
dp[2][1] = stair[2]
dp[2][2] = stair[1]+stair[2]
for i in range(3,N+1):
    dp[i][1] = stair[i] + max(dp[i-2][1], dp[i-2][2])
    dp[i][2] = stair[i] + dp[i-1][1]
print(max(dp[N][1], dp[N][2]))