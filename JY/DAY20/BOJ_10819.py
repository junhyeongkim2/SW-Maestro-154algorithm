import sys
import itertools
input = sys.stdin.readline

total = int(input())
t = list(map(int, input().split()))
t.sort()
per = itertools.permutations(t, total)
maxnum = 0
for i in per:
    num = 0
    for j in range(len(i)-1):
        num= num + abs(i[j] - i[j+1])
    
    if maxnum < num:
        maxnum = num
print(maxnum)

        