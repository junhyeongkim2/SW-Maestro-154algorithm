n,m=map(int,input().split())
li=[list(map(int,input())) for _ in range(n)]
ans=0

#|||
for i in range(1,m-1):
	for j in range(i+1,m):
		a=sum(li[y][x] for y in range(n) for x in range(i))
		b=sum(li[y][x] for y in range(n) for x in range(i,j))
		c=sum(li[y][x] for y in range(n) for x in range(j,m))
		ans=max(ans,a*b*c)

#☰
for i in range(1,n-1):
	for j in range(i+1,n):
		a=sum(li[y][x] for y in range(i) for x in range(m))
		b=sum(li[y][x] for y in range(i,j) for x in range(m))
		c=sum(li[y][x] for y in range(j,n) for x in range(m))
		ans=max(ans,a*b*c)

#ㅏ
for i in range(1,n):
	for j in range(1,m):
		a=sum(li[y][x] for y in range(n) for x in range(j))
		b=sum(li[y][x] for y in range(i) for x in range(j,m))
		c=sum(li[y][x] for y in range(i,n) for x in range(j,m))
		ans=max(ans,a*b*c)

#ㅓ
for i in range(1,n):
	for j in range(1,m):
		a=sum(li[y][x] for y in range(i) for x in range(j))
		b=sum(li[y][x] for y in range(i,n) for x in range(j))
		c=sum(li[y][x] for y in range(n) for x in range(j,m))
		ans=max(ans,a*b*c)

#ㅜ
for i in range(1,n):
	for j in range(1,m):
		a=sum(li[y][x] for y in range(i) for x in range(m))
		b=sum(li[y][x] for y in range(i,n) for x in range(j))
		c=sum(li[y][x] for y in range(i,n) for x in range(j,m))
		ans=max(ans,a*b*c)

#ㅗ
for i in range(1,n):
	for j in range(1,m):
		a=sum(li[y][x] for y in range(i) for x in range(j))
		b=sum(li[y][x] for y in range(i) for x in range(j,m))
		c=sum(li[y][x] for y in range(i,n) for x in range(m))
		ans=max(ans,a*b*c)

print(ans)
