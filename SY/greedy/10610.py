n=list(map(int,input()))
ans=0

if sum(n)%3!=0 or 0 not in n:
	print(-1)
	exit()
else:
	n.sort(reverse=True)
	for i in n:
		print(i,end='')