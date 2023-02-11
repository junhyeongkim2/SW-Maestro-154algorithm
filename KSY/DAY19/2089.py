N = int(input())
result = []

if N == 0:
    print(0)

while N != 0:
    if N % -2 == 0:
        result.append("0")
        N //= -2
    else:
        result.append("1")
        N //= -2
        N += 1

for i in reversed(result):
    print(i, end="")