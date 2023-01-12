import sys
input = sys.stdin.readline

N = int(input())
box = []
for _ in range(N):
  x = int(input())
  box.append(x)
box.sort()
for _ in range(N):
  print(box[_])