import sys

n,b=map(int,sys.stdin.readline().split())
num='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
li=[]

while n!=0:
	li.append(n%b)
	n=n//b
li.reverse()

for i in li:
	print(num[i],end='')