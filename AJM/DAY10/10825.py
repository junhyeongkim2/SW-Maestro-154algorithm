#10825 국영수
#파이썬 정렬할 때 앞에 -가 붙으면 감소(내림차순) +면 증가(오름차순)하는 순

import sys

n = int(input())
arr = []
for i in range(n):
    name, kor, eng, math = map(str,sys.stdin.readline().split())
    arr.append([name,int(kor),int(eng),int(math)])
    
arr.sort(key=lambda x: (-x[1],x[2],-x[3],x[0]))

for i in arr:
    print(i[0])