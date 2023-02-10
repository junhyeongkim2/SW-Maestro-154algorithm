"""
DP 2 X N 타일
N이 1일 때 - 1가지
N이 2일 때 - 2가지
N이 3일 때 - 3가지
N이 4일 때 - 5가지
....
피보나치 수열이 만들어지므로 DP로 사용된다.
"""
import sys
input = sys.stdin.readline

n = int(input())
d = [0] * 1001

d[1] = 1
d[2] = 2

for i in range(3, n+1):
    d[i] = d[i-1] +  d[i-2]
print(d[n]% 10007)
