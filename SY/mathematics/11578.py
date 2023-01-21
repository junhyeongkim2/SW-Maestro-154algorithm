a,b=map(int,input().split())
m=int(input())
li=list(map(int,input().split()))

ten,tmp=0,0
for i in li[::-1]:
	ten+=i*(a**tmp)
	tmp+=1

anw=[]
while ten!=0:
	anw.append(ten%b)
	ten//=b

for i in anw[::-1]:
	print(i,end=' ')
