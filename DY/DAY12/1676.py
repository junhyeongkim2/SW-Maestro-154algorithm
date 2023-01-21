import sys
input = sys.stdin.readline

N = int(input())

if N == 1:
    exit()

nums = [2, 5]
diction = {2:0, 5:0}
result = []
for n in range(1, N+1):
    for i in nums:
        while n % i == 0:
            n /= i
            diction[i] += 1

print(min(diction.values()))