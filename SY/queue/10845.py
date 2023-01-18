import sys

n=int(sys.stdin.readline())
li=[sys.stdin.readline().strip('\n') for _ in range(n)]
que=[]
for i in li:
	if 'push' in i:
		que.append(i[5:])
	elif i=='pop':
		if que:
			print(que.pop(0))
		else:
			print(-1)
	elif i=='size':
		print(len(que))
	elif i=='empty':
		if not que:
			print(1)
		else:
			print(0)
	elif i=='front':
		if que:
			print(que[0])
		else:
			print(-1)
	elif i=='back':
		if que:
			print(que[-1])
		else:
			print(-1)