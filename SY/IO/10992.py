n=int(input())
for i in range(1,n):
	print(' '*(n-i),end='')
	print('*',end='')
	print(' '*((i-1)*2-1),end='')
	if(i==1):
		print()
	else:
		print('*')
print('*'*((n*2)-1))