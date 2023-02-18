import math
from collections import deque

prime=[True for _ in range(10000)]
for i in range(10000):
	for j in range(2,int(math.sqrt(i))+1):
		if i%j==0:
			prime[i]=False
			break

def bfs(m):
	while deq:
		v=deq.popleft()
		if v==m:
			return visit[m]-1

		v=str(v)
		for i in range(4):
			for j in range(10):
				num=int(v[:i]+str(j)+v[i+1:])

				if num>1000 and not visit[num] and prime[num]:
					deq.append(num)
					visit[num]=visit[int(v)]+1

for _ in range(int(input())):
	n,m=map(int,input().split())
	visit=[0 for _ in range(10000)]
	visit[n]=1
	deq=deque([n])

	ans=bfs(m)
	if ans==None:
		print("Impossible")
	else:
		print(ans)
