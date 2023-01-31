N = int(input())
dp = [-1] * 1000001 #10^6 + 1 주의

# 재귀로 구현했으나 재귀 허용 범위를 넘었기 때문에 반복문으로 다시 구현
# def f(n):
#     if n == 1:
#         return 0
#     if dp[n] != -1:
#         return dp[n]
#
#     result = f(n - 1) + 1
#     if n % 3 == 0:
#         result = min(result, f(n // 3) + 1)
#     if n % 2 == 0:
#         result = min(result, f(n // 2) + 1)
#
#     dp[n] = result
#     return result
#
#
# print(f(N))
if N == 1:
    print(0)
else:
    dp[1] = 0
    for i in range(2, N+1):
        if dp[i] != -1:
            pass

        result = dp[i-1] + 1
        if i % 3 == 0:
            result = min(result, dp[i//3] + 1)
        if i % 2 == 0:
            result = min(result, dp[i//2] + 1)

        dp[i] = result

    print(dp[N])
