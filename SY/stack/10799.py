li=list(input())
cnt=0
stack=[]
for i in range(len(li)):
	if li[i]=='(':
		stack.append(li[i])
	if li[i]==')':
		if li[i-1]=='(':
			stack.pop()
			cnt+=len(stack)
		elif li[i-1]==')':
			stack.pop()
			cnt+=1
print(cnt)