import sys

n=int(sys.stdin.readline())
star=[[' ']*2*n for _ in range(n)]

def divconq(x,y,n):
	if n==3:
		star[y][x]='*'
		star[y+1][x-1]=star[y+1][x+1]='*'
		star[y+2][x-2:x+3]=['*','*','*','*','*']
	else:
		divconq(x,y,n//2) #상단
		divconq(x-(n//2),y+(n//2),n//2) #하단 좌측
		divconq(x+(n//2),y+(n//2),n//2) #하단 우측

divconq(n-1,0,n)

for i in star:
	print("".join(i))