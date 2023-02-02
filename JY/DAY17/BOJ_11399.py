import sys

input = sys.stdin.readline

total = int(input())
line = list(map(int, input().split()))

line.sort()
res = []
sum = 0
for i in line:
    sum += i
    res.append(sum)

ans = 0
for r in res:
    ans += r
print(ans)