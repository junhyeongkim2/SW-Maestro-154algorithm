from collections import deque
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
visitnum=[0 for _ in range(100001)]

def bfs(n):
	deq=deque([n])
	
	while deq:
		v=deq.popleft()

		if v==m:
			return visitnum[v]

		pos=[v-1,v+1,v*2]

		for i in pos:
			if 0<=i<=100000 and not visitnum[i]:
				visitnum[i]=visitnum[v]+1
				deq.append(i)

print(bfs(n))