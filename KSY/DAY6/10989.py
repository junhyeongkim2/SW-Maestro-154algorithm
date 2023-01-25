from sys import stdin
n = int(stdin.readline())
numbers = {}
for _ in range(n):
    number = int(stdin.readline())
    if number not in numbers:
        numbers[number] = 1
    else:
        numbers[number] += 1

numberList = sorted(numbers.items())

for i, n in numberList:
    for _ in range(n):
        print(i)
