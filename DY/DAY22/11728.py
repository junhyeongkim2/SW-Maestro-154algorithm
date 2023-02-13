# 11728번 배열 합치기
# https://www.acmicpc.net/problem/11728

N, M = map(int, input().split())

arr = list(map(int, input().split())) + list(map(int, input().split()))
print(*sorted(arr))