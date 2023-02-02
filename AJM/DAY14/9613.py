#9613 GCD 합
import itertools
import math

n = int(input())

for i in range(n):
    arr = list(map(int,input().split()))
    all = itertools.combinations(arr[1:],2)
    all = list(all)
    answer = 0
    for i in all:
        answer += math.gcd(i[0],i[1])
    print(answer)
