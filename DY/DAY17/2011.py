# 2011번 암호코드
# https://www.acmicpc.net/problem/2011

code = list(map(int, input()))
N = len(code)

if code[0] == 0:
    print(0)
    exit()

if N==1:
    print(1)
    exit()

dp = [0] * (N)
dp[0] = 1
dp[1] = 1
if code[1] != 0: # 연속으로 해석할 수 있는 경우
    if code[0] == 1 or (code[0] == 2 and code[1] <= 6):
        dp[1] += 1
elif code[0]!=1 and code[0]!=2:
    print(0)
    exit()

for i in range(2, N):
    if code[i] != 0:
        if code[i-1] == 1 or (code[i-1] == 2 and code[i] <= 6): # 연속으로 해석할 수 있는 경우
            dp[i] = (dp[i-1] + dp[i-2])%1000000
        else: dp[i] = dp[i-1]
    else: # 0인 경우
        if code[i-1]==1 or code[i-1]==2:
            dp[i] = dp[i-2]
        else:
            print(0)
            exit()
print(dp[N-1])