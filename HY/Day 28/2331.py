import sys
input = sys.stdin.readline

a, p = map(int, input().split())
arr=[a]

while True:
    sum = 0
    stra =list(str(a))
    for i in stra: #수를 곱해주고 배열에 넣어줌
        sum += int(i) ** p
    if sum in arr:
        start = arr.index(sum)
        print(arr)
        del arr[start:-1]
        break
    else:
        arr.append(sum)  
        a = arr[-1]  

print(len(arr)-1)


    