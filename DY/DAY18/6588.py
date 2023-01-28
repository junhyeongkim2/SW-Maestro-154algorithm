# 6588번 골드바흐의 추측
# https://www.acmicpc.net/problem/6588
import math
import sys
read = sys.stdin.readline

def isPrime(num):
    for i in range(2, math.floor(num**(1/2))+1):
        if num % i == 0: return False
    return True

nums = []
while True:
    n = int(read().strip())
    if n==0: break
    nums.append(n)

prime = []
for n in range(3, max(nums)):
    if isPrime(n): prime.append(n)

for num in nums:
    for p in prime:
        if (num//2)+1 <= p:
            print("Goldbach's conjecture is wrong.")
            break
        elif isPrime(num-p):
            print(f'{num} = {p} + {num-p}')
            break