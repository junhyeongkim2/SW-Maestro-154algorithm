import sys

input = sys.stdin.readline
M, N = map(int, input().split())
if M < N: # M이 더 큰 수가 되도록 함
    M, N = N, M

def gcd(M, N):
    if M % N == 0:
        return N
    else:
        return gcd(N, M % N)
print(gcd(M,N))
print(M*N//gcd(M,N))