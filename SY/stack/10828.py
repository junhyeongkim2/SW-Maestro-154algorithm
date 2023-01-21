n=int(input())
li=[input() for _ in range(n)]
stack=[]

for i in li:
	if 'push' in i:
		stack.append(int(i[5:]))
	elif i=='pop':
		if not stack:
			print(-1)
		else:
			print(stack.pop())
	elif i=='size':
		print(len(stack))
	elif i=='empty':
		if not stack:
			print(1)
		else:
			print(0)
	else:
		if not stack:
			print(-1)
		else:
			print(stack[-1])
