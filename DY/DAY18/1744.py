# 1744 수 묶기
# https://www.acmicpc.net/problem/1744
import sys
read = sys.stdin.readline
N = int(read().strip())

neg = []
pos = []
one = 0

for _ in range(N):
    num = int(read().strip())
    if num<=0: neg.append(num)
    elif num==1: one+=1
    else: pos.append(num)

neg.sort(reverse=True)
pos.sort()
res = 0
while len(neg)>1: # 음수 계산
    res += neg.pop()*neg.pop()
if len(neg)==1: # neg가 남았는데 zero가 있을 시
    res += neg[0]
res += one
while len(pos)>1: # 음수 계산
    res += pos.pop()*pos.pop()
if len(pos)==1:
    res += pos[0]
print(res)