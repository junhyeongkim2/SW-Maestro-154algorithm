import sys
n=int(input())
li=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
li.sort()

for i in range(n):
	for j in range(2):
		print(li[i][j],end=' ')
	print()