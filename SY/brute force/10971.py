import sys
input=sys.stdin.readline

n=int(input())
city=[list(map(int,input().split())) for _ in range(n)]
m=sys.maxsize

def dfs(start,next,cost,visit):
	global m

	if len(visit)==n:
		if city[next][start]!=0:
			m=min(m,cost+city[next][start])
		return

	for i in range(n):
		if i not in visit and city[next][i]!=0 and cost<m:
			visit.append(i)
			dfs(start,i,cost+city[next][i],visit)
			visit.pop()

for i in range(n):
	visit=[i]
	dfs(i,i,0,visit)

print(m)