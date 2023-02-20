"""
외판원 순회 2
"""
import sys
input = sys.stdin.readline
from itertools import permutations
arr =[]

n = int(input())

for i in range(4):
    arr.append(int, input().split())

answer = sys.maxsize
sum = list(permutations(arr,n))
