from collections import deque
import sys

n,k=map(int,sys.stdin.readline().split())
deq=deque([i for i in range(1,n+1)])
yo=[]

while deq:
	deq.rotate(-k+1)
	yo.append(str(deq.popleft()))

sys.stdout.write("<"+", ".join(yo)+">")