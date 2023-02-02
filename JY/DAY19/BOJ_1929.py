import sys
import math

input = sys.stdin.readline
A, B= map(int, input().split())

arr = [True] * (B+1)


for i in range(2, int(math.sqrt(B))+1):
    if arr[i] == True:
        j = 2
        while i * j <= B:
            arr[i*j] = False
            j+=1

for k in range(A, len(arr)):
    if arr[k] == True:
        print(k)