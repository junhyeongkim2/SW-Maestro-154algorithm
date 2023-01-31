import sys

input = sys.stdin.readline

M = int(input())
tmp = list(map(int, input().split()))
tmp.sort()
dic = {}        
for value in tmp:
    try: dic[value] += 1
    except: dic[value] = 1  

num = list(dic.keys())
N = int(input())
check = list(map(int, input().split()))


res = [0] * (N)
for k in range(N):
    start = 0
    end = len(num) -1
    while start <= end:
        mid = (start + end) // 2
        if check[k] == num[mid]:
            res[k] = dic.get(num[mid])
            break
        elif check[k] < num[mid]:
            end = mid -1
        else:
            start = mid +1
for i in res:
    print(i , end = " ")
            
        
    