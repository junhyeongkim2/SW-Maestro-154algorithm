# 2875번 대회 or 인턴
# https://www.acmicpc.net/problem/2875

N,M,K = map(int, input().split())
cnt = min(N//2, M)
while (N+M)-3*cnt < K:
    cnt-=1
print(cnt)