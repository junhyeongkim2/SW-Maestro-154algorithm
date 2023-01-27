import sys
from itertools import accumulate
input = sys.stdin.readline

n = int(input())
peopleTime = list(map(int, input().split()))
result = 0
peopleTime.sort()
peopleTime = accumulate(peopleTime)

for t in peopleTime:
    result += t

print(result)