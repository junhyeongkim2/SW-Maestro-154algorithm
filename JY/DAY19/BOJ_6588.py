import sys

input = sys.stdin.readline

arr = [False, False] + [True]*(1000000)
for i in range(2, 1001):
    if arr[i] == True:
        j = 2
        while j*i <= 1000000:
            arr[i*j] = False
            j += 1

while True:
    A = int(input())
    if A == 0:
        break
    for k in range(3, len(arr)):
        tmp = A - k
        if arr[k] == True and arr[tmp] == True:
            print("%d = %d + %d"%(A , k , tmp))
            break

                
    