import sys
input = sys.stdin.readline

N = int(input())
box = []

for i in range(N):
  x,y = map(int,input().split())
  box.append([y,x])
box.sort()

for i in range(N):
  print(box[i][1],box[i][0])
