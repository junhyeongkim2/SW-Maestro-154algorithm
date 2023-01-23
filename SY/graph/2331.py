a,p=map(int,input().split())
li=[a]

while True:
	n=li[-1]
	m=0
	while n!=0:
		m+=(n%10)**p
		n//=10
	if m in li:
		idx=li.index(m)
		break
	li.append(m)

print(idx)