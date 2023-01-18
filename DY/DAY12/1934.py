# 1934번 최소공배수
# https://www.acmicpc.net/problem/1934
import sys
read = sys.stdin.readline

def gdc(x, y): # 유클리드 호제법
    if y==0:
        return x
    return gdc(y, x%y)

for _ in range(int(read().strip())):
    A, B = map(int, read().split())
    print(A*B//gdc(A,B))

    # 시간초과
    # mul = 1
    # while True:
    #     if B*mul % A == 0:
    #         print(B * mul)
    #         break
    #     mul += 1