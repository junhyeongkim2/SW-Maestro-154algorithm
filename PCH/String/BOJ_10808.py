import sys
input = sys.stdin.readline
x = list(input().rstrip())

alp = [0]*26

for i in x:
  alp[ord(i)-97] += 1


for i in range(26):
  print(alp[i], end = ' ')
