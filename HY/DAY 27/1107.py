import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
broken = list(map(str,input().split()))
result = abs(100-n)

for i in range(1000000):
  for j in str(i):
    if j in broken:
      break
    else:
      result = min(result, len(str(i)) + abs(i-n))
print(result)