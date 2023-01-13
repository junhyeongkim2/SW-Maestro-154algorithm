import sys
input = sys.stdin.readline

N = int(input())

# index와 값을 매칭시키고 개수만큼 1 증가
box = [0]*10001
for i in range(N):
  index = int(input())
  box[index] += 1

for i in range(1, 10001):
  if box[i] != 0:
    for k in range(box[i]):
      print(i)