"""
N개의 정수로 이루어진 수열이 있을 때, 
크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.
부분 수열의 합
"""
import sys
input = sys.stdin.readline
from itertools import combinations #조합 라이브러리

n,s = map(int, input().split()) # 정수의 개수 n, 만들고자하는 합 s
arr = list(map(int, input().split())) #수열
cnt = 0 # 합이 s가 되는 부분 수열의 개수 

for i in range(1,n+1): #1부터 n+1까지
    c = list(combinations(arr,i)) #수열을 조합으로 만듬, 1개의 조합부터 n개까지의 조합을 만듬
    
    for j in c: #위에서 만든 i개의 원소를 가지는 조합을 하나씩 돌아봄
      if sum(j) == s: #s가 되면
        cnt += 1 #카운트

print(cnt)
    
