import sys

st=list(sys.stdin.readline().strip('\n'))
n=int(sys.stdin.readline())
li=[sys.stdin.readline().strip('\n') for _ in range(n)]
stack=[]

for i in li:
	if 'P' in i:
		st.append(i[2:])
	elif i=='B':
		if st:
			st.pop()
	elif i=='L':
		if st :
			stack.append(st.pop())
	elif i=='D':
		if stack:
			st.append(stack.pop())
for i in range(len(stack)):
	st.append(stack.pop())

for i in st:
	print(i,end='')