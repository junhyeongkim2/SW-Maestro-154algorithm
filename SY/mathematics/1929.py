m,n=map(int,input().split())

for i in range(m,n+1):
	if i==1:
		continue
	for j in range(2,int(i**0.5)+1): #에라토스테네스의 체
		if i%j==0:
			break
	else:
		print(i)
