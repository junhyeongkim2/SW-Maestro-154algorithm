import sys
input = sys.stdin.readline

N = int(input())
box = []

for i in range(N):
  x,y = map(int,input().split())
  box.append([x,y])
box.sort()

for i in range(N):
  print(box[i][0],box[i][1])
