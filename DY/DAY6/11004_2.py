# 11004번 K번째 수
# https://www.acmicpc.net/problem/11004

_, K = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
print(arr[K-1])