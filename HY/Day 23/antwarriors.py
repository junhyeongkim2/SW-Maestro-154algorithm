#개미전사 문제
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

#앞에서 계산된 결과를 저장하기 위한 dp 테이블 
dp = [0] * 100

#보텀업 진행

dp[0] = arr[0]
dp[1] = max(arr[0], arr[1])
#dp[1]과 dp[0] + arr[2]의 합 중 더 큰 것을 dp[2]에 넣음
for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2]+ arr[i])
    print(dp[i])

print(dp[n-1])

