import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr1 = set(map(int, input().split()))
arr2 = set(map(int, input().split()))

arr1.update(arr2)
set(arr1)
print(*arr1)