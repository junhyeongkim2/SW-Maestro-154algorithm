import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

result = arr1 + arr2
result.sort()
print(*result)
