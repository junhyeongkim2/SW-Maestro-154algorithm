import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

dic = {}

for i in arr:
    if i in dic: #만약 딕셔너리에 값이 있으면 +1
        dic[i] += 1
    else: #없으면 그냥 1
        dic[i] = 1


for j in arr2:
  if j in dic: #딕셔너리에 arr2값이 있으면
    print(dic[j], end=' ') #몇개 있는지 출력, 예를들어 0번째 인덱스 0를 볼 때, dic[10] : 3이므로 3 출력
  else:
    print(0, end=" ")
