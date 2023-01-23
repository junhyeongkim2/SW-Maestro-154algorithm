import sys

n=int(input())
anw=[]

if n==0:
	print(0)
	exit()

while n!=0:
	anw.append(abs(n%-2))
	n//=-2
	if anw[-1]==1:
		n+=1

for i in anw[::-1]:
	print(i,end='')