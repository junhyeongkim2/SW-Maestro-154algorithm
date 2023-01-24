from sys import stdin
n = int(stdin.readline())
numbers = []
for _ in range(n):
    numbers.append(int(stdin.readline()))

numbers.sort()

for i in numbers:
    print(i)