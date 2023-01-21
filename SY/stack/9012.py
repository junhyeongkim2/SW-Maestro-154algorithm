n=int(input())
li=[list(input()) for _ in range(n)]

for i in range(n):
	stack=[]
	for j in li[i]:
		stack.append(j)
		if len(stack)>1:
			if stack[-2]=='(' and stack[-1]==')':
				stack.pop()
				stack.pop()
	if not stack:
		print('YES')
	else:
		print('NO')
