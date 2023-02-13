from itertools import permutations
import sys
input=sys.stdin.readline

n=int(input())
li=list(map(int,input().split()))
per=permutations(li)
ans=0

for i in per:
	tmp=0
	for j in range(len(i)-1):
		tmp+=abs(i[j]-i[j+1])
	ans=max(ans,tmp)

print(ans)
