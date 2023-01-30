#2751 수 정렬하기 2
import sys
n = int(input())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline().strip()))

arr.sort()
        
for i in range(n):
    print(arr[i])

