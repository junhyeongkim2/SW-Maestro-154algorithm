import sys
input = sys.stdin.readline
N = int(input())
box = []
for i in range(N):
  x,y = input().split()
  box.append([int(x),y])

box.sort(key = lambda x:x[0])

for item in box:
  print(item[0],item[1])