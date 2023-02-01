import sys
import math

input = sys.stdin.readline

l = int(input())
nums = list(map(int, input().split()))

arr = [True] * 1001
arr[0] = False
arr[1] = False

for i in range(2, int(math.sqrt(1000))+1):
    if arr[i] == True:
        j = 2
        while i*j <= 1000:
            arr[i*j] = False
            j+=1
cnt = 0
for n in nums:
    if arr[n] == True:
        cnt +=1
print(cnt)    