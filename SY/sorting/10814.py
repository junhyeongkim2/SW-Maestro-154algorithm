import sys
n=int(sys.stdin.readline())
li=[list(sys.stdin.readline().split()) for _ in range(n)]
for i in range(n):
	li[i][0]=int(li[i][0])
li.sort(key=lambda x:x[0])
for i in range(n):
	for j in range(2):
		print(li[i][j], end=' ')
	print()