n=int(input())
li=list(map(int,input().split()))
asc=[0]*n
desc=[0]*n
asc[0]=desc[0]=1
cnt=0

for i in range(1,n):
	for j in range(i):
		if li[j]<li[i]:
			asc[i]=max(asc[i],asc[j])
	asc[i]+=1
	
li.reverse()
for i in range(1,n):
	for j in range(i):
		if li[j]<li[i]:
			desc[i]=max(desc[i],desc[j])
	desc[i]+=1

desc.reverse()

for i in range(n):
	cnt=max(cnt,asc[i]+desc[i]-1)
print(cnt)
