n, number = map(int, input().split())
coinType, result = [], 0
for _ in range(n):
    coinType.append(int(input()))

for i in reversed(coinType):
    result += number//i
    number %= i

print(result)