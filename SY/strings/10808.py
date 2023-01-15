st=list(input())
alpha=[0]*26

for i in range(len(st)):
	alpha[ord(st[i])-97]+=1

for i in alpha:
	print(i,end=' ')