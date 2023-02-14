n,m,k=map(int,input().split())
cnt=0

while True:
	if n>1 and m>0 and n+m-3>=k:
		cnt+=1
		n-=2
		m-=1
	else:
		break
print(cnt)
