import sys
input = sys.stdin.readline
N, M = map(int, input().split())

alist = list(map(int, input().split())) #N개 원소
alist += list(map(int, input().split())) #M개 원소

alist.sort()
for n in alist:
    print(n, end=" ")