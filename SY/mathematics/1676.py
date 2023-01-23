n=int(input())
cnt=1
for i in range(2,n+1):
	cnt*=i

z=0
while True:
	if cnt%10==0:
		cnt//=10
		z+=1
	else:
		print(z)
		break