y,x=map(int,input().split())

if y==1:
	print(1)
elif y==2:
	if x<3:
		print(1)
	else:
		print(min(4,(x+1)//2))
else:
	if x<7:
		print(min(x,4))
	else:
		print(x-2)
	