n = int(input())
numbers = list(map(int, input().split()))
result = 0

for i in numbers:
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        result += 1

print(result)