# 2745 진법 변환 2
# https://www.acmicpc.net/problem/2745

N, B = input().split()
B = int(B)
ans = 0
for i in range(len(N)):
    if ord(N[i])>=65: # 알파벳인 경우
        ans += B ** (len(N) - i - 1) * (ord(N[i])-55)
    else: ans += B ** (len(N) - i - 1)*int(N[i])
print(ans)
