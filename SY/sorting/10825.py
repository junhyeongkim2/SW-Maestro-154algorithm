import sys
n=int(sys.stdin.readline())
li=[list(input().split()) for _ in range(n)]

for i in range(n):
	li[i][1]=int(li[i][1])
	li[i][2]=int(li[i][2])
	li[i][3]=int(li[i][3])

li.sort(key=lambda x:x[0])
li.sort(reverse=True, key=lambda x:x[3])
li.sort(key=lambda x:x[2])
li.sort(reverse=True, key=lambda x:x[1])

for i in range(n):
	print(li[i][0])