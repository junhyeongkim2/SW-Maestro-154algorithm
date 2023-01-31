#11650 좌표 정렬하기
import sys

n = int(input())
arr =[]
for i in range(n):
    arr.append(list(map(int,input().split())))

arr.sort()

for i in arr:
    print(i[0],i[1])
    