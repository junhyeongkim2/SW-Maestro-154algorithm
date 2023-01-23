n=int(input())
li=list(map(int,input().split()))
if 1 in li:
	li.remove(1)
cnt=0
for i in li:
	tmp=0
	for j in range(2,i):
		if i%j==0:
			tmp=1
			break
	if tmp==0:
		cnt+=1
print(cnt)