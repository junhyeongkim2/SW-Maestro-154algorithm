import sys

input = sys.stdin.readline
A, B = map(int, input().split())

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
res = list1 + list2
res.sort()

for r in res:
    print(r, end = " ")