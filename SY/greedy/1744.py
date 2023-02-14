import sys
input=sys.stdin.readline

num=int(input())
p=[]
n=[]
cnt=0
for _ in range(num):
	k=int(input())

	if k>1:
		p.append(k)
	elif k==1:
		cnt+=1	
	else:
		n.append(k)

n.sort()
p.sort(reverse=True)

#음수가 짝수 개 일 때
if len(n)!=0 and len(n)%2==0:
	for i in range(0,len(n)-1,2):
		cnt+=n[i]*n[i+1]

#음수가 홀수 개 일 때
elif len(n)!=0 and len(n)%2==1:
	for i in range(1,len(n)-1,2):
		cnt+=n[i-1]*n[i]
	cnt+=n[-1]

#양수가 짝수 개 일 때
if len(p)!=0 and len(p)%2==0:
	for i in range(0,len(p)-1,2):
		cnt+=p[i]*p[i+1]

#양수가 홀수 개 일 때
elif len(p)!=0 and len(p)%2==1:
	for i in range(1,len(p)-1,2):
		cnt+=p[i-1]*p[i]
	cnt+=p[-1]

print(cnt)
