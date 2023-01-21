import sys
n,b=sys.stdin.readline().split()
num='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

anw=0
tmp=1
for i in n[::-1]:
	anw+=num.index(i)*tmp
	tmp*=int(b)
print(anw)