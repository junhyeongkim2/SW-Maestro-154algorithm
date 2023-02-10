# n=1
# while True:
# 	if n*n<100000:
# 		print(n)
# 		n+=1
# 	else:
# 		break
n=int(input())
dp=[0]*(n+1)
square=[i*i for i in range(1,317)]

for i in range(1,n+1):
	tmp=[]
	for j in square:
		if j>i:
			break
		tmp.append(dp[i-j])
	dp[i]=min(tmp)+1

print(dp[n])
