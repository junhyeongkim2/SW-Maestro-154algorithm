import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def dfs(n):
	visit[n]=True
	cyc.append(n)

	if not visit[li[n]]:
		dfs(li[n])
	elif cyc[0]==li[n]:
		return

for _ in range(int(input())):
	n=int(input())
	li=[0]+list(map(int,input().split()))
	visit=[False]*(n+1)

	cnt=0
	for i in range(1,n+1):
		if not visit[i]:
			cyc=[]
			cnt+=1
			dfs(i)
	print(cnt)