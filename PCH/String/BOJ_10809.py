import sys
input = sys.stdin.readline
x = list(input().rstrip())

alp = [-1]*26
cnt=0

for i in x:
  if (alp[ord(i)-97] == -1):
    alp[ord(i)-97] = cnt
  cnt += 1


for i in range(26):
  print(alp[i], end = ' ')
