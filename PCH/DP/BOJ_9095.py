import sys
input = sys.stdin.readline

t = int(input())

def solve(n):
  if n == 1:
    return 1
  if n == 2:
    return 2
  if n == 3:
    return 4
  
  return solve(n-1) + solve(n-2) + solve(n-3)

for i in range(t):
  n = int(input())
  print(solve(n))