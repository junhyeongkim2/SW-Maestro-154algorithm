from collections import deque

n,k=map(int,input().split())
deq=deque([i for i in range(1,n+1)])
yo=[]

for i in range(n):
	for j in range(1,k):
		deq.append(deq.popleft())
	yo.append(deq.popleft())

print('<',end='')
for i in range(n-1):
	print(yo[i],end=', ')
print(yo[-1],end='>')