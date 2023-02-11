import math
import sys

input = sys.stdin.readline

testCase = int(input())
for _ in range(testCase):
    numbers = list(map(int, input().split()))
    gcdSum = 0
    for i in range(1, numbers[0]+1):
        for j in range(i+1, numbers[0]+1):
            gcdSum += math.gcd(numbers[i], numbers[j])
    print(gcdSum)