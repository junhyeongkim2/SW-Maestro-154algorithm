n=int(input())
li=list(map(int,input().split()))
li.sort()
cnt=0

for i in range(n):
	tmp=0
	for j in range(i+1):
		tmp+=li[j]
	cnt+=tmp
print(cnt)