n=int(input())
star=[[' ']*n for _ in range(n)]

def divconq(n):
	if n==3:
		star[0][:3]=['*','*','*']
		star[1][:3]=['*',' ','*']
		star[2][:3]=['*','*','*']
		return

	divconq(n//3)

	for i in range(3):
		for j in range(3):
			if i==1 and j==1:
				continue

			for z in range(n//3):
				star[z+i*(n//3)][j*(n//3):(j+1)*(n//3)]=star[z][0:n//3]
divconq(n)
for i in star:
	for j in i:
		print(j,end='')
	print()