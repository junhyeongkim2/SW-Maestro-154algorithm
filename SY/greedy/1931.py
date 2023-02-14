import sys
input=sys.stdin.readline

n=int(input())
li=[list(map(int,input().split())) for _ in range(n)]
li.sort(key=lambda x: x[0])
li.sort(key=lambda x: x[1])

cnt,end=0,0
for i in range(n):
	if end<=li[i][0]:
		cnt+=1
		end=li[i][1]

print(cnt)