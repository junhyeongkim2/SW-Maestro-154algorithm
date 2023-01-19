import sys
from itertools import combinations
read = sys.stdin.readline

def gdc(x,y):
    if y==0: return x
    return gdc(y, x%y)

for _ in range(int(read().strip())):
    nums = list(map(int,read().split()))[1:]
    comb = combinations(nums,2)
    ans = 0
    for x, y in comb:
        ans += gdc(x,y)
    print(ans)