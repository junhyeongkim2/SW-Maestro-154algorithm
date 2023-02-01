import sys

input = sys.stdin.readline

total = int(input())

pos = []
neg = []
for _ in range(total):
    t = int(input())
    if t > 0:
        pos.append(t)
    else:
        neg.append(t)


pos.sort(reverse = True)
neg.sort()
num = pos+ neg

res = 0
for p in range(0, len(pos), 2):
    if p == len(pos)-1:
        res = res + pos[p]
    else:
        a = pos[p]
        b = pos[p+1]
        if a == 1 or b == 1:
            res = res + a + b
        else:
            res = res + a*b
    
for n in range(0, len(neg),2):
    if n == len(neg)-1:
        res = res+neg[n]
    else:
        res = res + neg[n] * neg[n+1]

print(res)
        