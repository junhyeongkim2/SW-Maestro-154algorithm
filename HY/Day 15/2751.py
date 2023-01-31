import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
  arr.append(int(input()))

arr.sort()
for i in arr:
  print(i)