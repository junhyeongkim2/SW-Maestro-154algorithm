import sys
input=sys.stdin.readline

n=int(input())
li=[list(map(int,input().split())) for _ in range(n)]
paper=[0,0,0] #-1, 0, 1

def divconq(x,y,n):
	#전체 종이 검사
	tmp=1
	num=li[y][x]
	for i in range(y,y+n):
		for j in range(x,x+n):
			if li[i][j]!=num:
				tmp=0
				break

	#종이 분할 및 확인 시작
	if tmp==0:
		for i in range(3):
			for j in range(3):
				divconq(x+j*(n//3), y+i*(n//3), n//3)
		return

	if num==-1:
		paper[0]+=1
	elif num==0:
		paper[1]+=1
	else:
		paper[2]+=1

divconq(0,0,n)
for i in paper:
	print(i)
