import sys

n=int(sys.stdin.readline())
dic={0:0}
for i in range(n):
	m=int(sys.stdin.readline())
	if m not in dic.keys():
		dic[m]=0
	dic[m]+=1
li=sorted(dic.items())

mxcnt=0
mxnum=0
for i in li:
	if i[1]>mxcnt:
		mxcnt=i[1]
		mxnum=i[0]

print(mxnum)