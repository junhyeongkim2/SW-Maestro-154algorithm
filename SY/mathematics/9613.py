import math

n=int(input())

for i in range(n):
	li=list(map(int,input().split()))
	gcd=0
	for j in range(1,len(li)-1):
		for z in range(j+1,len(li)):
			gcd+=math.gcd(li[j],li[z])
	print(gcd)