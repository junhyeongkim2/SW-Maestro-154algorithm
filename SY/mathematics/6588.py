import sys
li=[True for i in range(1000001)]

for i in range(2,int(1000001**0.5)+1):
	if li[i]==True:
		for j in range(i*2,1000001,i):
			li[j]=False

while True:
	n=int(sys.stdin.readline())
	if n==0:
		break

	for i in range(3,1000001):
		if li[i] and li[n-i]:
			print(n,'=',i,'+',n-i)
			break