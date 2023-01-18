import sys
input = sys.stdin.readline

N = int(input())

if N == 1:
    exit()

result = []
for i in range(2, N+1):
    while N % i == 0:
        N /= i
        result.append(i)

for r in result:
    print(r)