"""
1, 2, 3 더하기 DP
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하시오
점화식
d[i] = d[i-1] + d[i-2] + d[i-3]
만약 4를 구한다면
7의 합의 갯수 = 6의 합 + 5의 합 + 4의합
"""

import sys
input = sys.stdin.readline

d = [0] * 11
d[1], d[2], d[3] = 1, 2, 4

for i in range(4, 11):
    d[i] = d[i-1] + d[i-2] + d[i-3]

n = int(input())

for i in range(n):
    m = int(input())
    print(d[m])
