from sys import stdin
n = int(input())
numbers = {}

for i in range(n):
    number = int(stdin.readline())
    if number not in numbers:
        numbers[number] = 1
    else:
        numbers[number] += 1

numbersList = sorted(numbers.items(), key=lambda x: (-x[1], x[0]))
print(numbersList[0][0])
