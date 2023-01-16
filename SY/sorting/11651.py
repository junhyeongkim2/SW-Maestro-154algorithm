import sys
n=int(sys.stdin.readline())
li=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
li.sort()
li.sort(key=lambda x:x[1])

for i in range(n):
	for j in range(2):
		print(li[i][j],end=' ')
	print()