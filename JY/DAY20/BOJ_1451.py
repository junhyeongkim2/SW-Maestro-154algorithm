import sys

input = sys.stdin.readline

w, h = map(int, input().split())

arr= []
for i in range(h):
    arr.append(list(map(int, input().split())))

if w >= 2 and h >= 2:
    #하나 고정하고 직사각형 만들기 
    for q in range(w):
        tmp1 = sum(arr[0][:q])
        if q == w-1:
            tmp2 = sum(arr[])
#1 가로 3개

for j in range(w-1):
    for k in range(j+1, w):
        tmp1 = sum(arr[:j])
        tmp2 = sum(arr[j+1:k])
        tmp3 = sum(arr[k+1:])
        res = max(res, tmp1*tmp2*tmp3)           
elif w == 1:
    for j in range(h -2):
        for k in range(j+1, h):
            res = max(res, arr[:j][0] +  + arr[k+1:][0])   
