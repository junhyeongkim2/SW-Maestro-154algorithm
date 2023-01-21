import sys
input = sys.stdin.readline
N = int(input())
box = {}
for i in range(N):
  index = int(input())
  if index in box:
    box[index] += 1
  else:
    box[index] = 1
result = sorted(box.items(), key = lambda x: (-x[1], x[0]))

print(result[0][0])