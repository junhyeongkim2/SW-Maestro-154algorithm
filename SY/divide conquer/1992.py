n=int(input())
li=[list(map(int,input())) for _ in range(n)]
ans=[]

def divconq(x,y,n):
	tmp=1
	dot=li[y][x]
	for i in range(y,y+n):
		for j in range(x,x+n):
			if li[i][j]!=dot:
				tmp=0
				break

	if tmp==0:
		print('(',end='')
		for i in range(2):
			for j in range(2):
				divconq(x+j*(n//2),y+i*(n//2),n//2)
		print(')',end='')
	else:
		print(dot,end='')


divconq(0,0,n)