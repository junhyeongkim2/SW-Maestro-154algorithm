#1158 요세푸스 문제
n,k = map(int,input().split())
arr=[i for i in range(1,n+1)]

answer = []
num = 0
for i in range(n):
    num += k-1
    if num >= len(arr):
        num %= len(arr)
    answer.append(arr.pop(num))

print(str(answer).replace("[","<").replace("]",">"))

"""
다른 풀이

deque 클래스에 rotate은 원형 리스트처럼 회전이 가능함.
tabl
#1168 요세푸스 문제 2
import sys
from collections import deque
n,k = map(int,sys.stdin.readline().split())
arr=deque([i for i in range(1,n+1)])
answer = []
num = 0

while(arr):
    arr.rotate(-k+1)
    answer.append(arr.popleft())
"""