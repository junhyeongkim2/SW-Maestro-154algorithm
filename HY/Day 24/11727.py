"""
DP 2 X N 타일 2
N이 1일 때 - 1가지
N이 2일 때 - 3가지
N이 3일 때 - 5가지
N이 4일 때 - 11가지
점화식
 d[i] = d[i-1] + (2 * d[i-2])
4의 타일 합 = 3의합 + 2 * 2의 합
"""

import sys
input = sys.stdin.readline

n = int(input())
d = [0] * 11
d[1], d[2] = 1, 3

for i in range(3, n+1):
    d[i] = d[i-1] + (2 * d[i-2])

print(d[n] % 10007)
