n=int(input())
m=int(input())
if m:
	li=list(map(str,input().split()))
else:
	li=[]
cnt=abs(100-n)

for i in range(1000001):
	for j in str(i):
		if j in li:
			break
	else:
		cnt=min(cnt, abs(i-n)+len(str(i)))
print(cnt)
