# i=0
# while True:
# 	print(i)
# 	i+=1
# 	if i**2>100000:
# 		break
square=[i**2 for i in range(1,317)]
n=int(input())
dp=[0]*(n+1)

for i in range(1,n+1):
	tmp=[]
	for j in square:
		if j>i:
			break
		tmp.append(dp[i-j])
	dp[i]=min(tmp)+1
	
print(dp[n])