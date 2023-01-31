import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
  age,name = input().split()
  arr.append([int(age),name])

#SORT를 사용하면 알파벳순 정렬도 가능
arr.sort(key=lambda x:(x[0]))

for i in arr:
  print(i[0],i[1])