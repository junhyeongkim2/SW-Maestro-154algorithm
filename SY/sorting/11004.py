import sys
n,k=map(int,sys.stdin.readline().split())
li=list(map(int,sys.stdin.readline().split()))
li.sort()
print(li[k-1])