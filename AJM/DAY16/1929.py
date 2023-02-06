# 1929 소수 구하기

a, b = map(int, input().split())
num = [0] * 1000001
for i in range(a, b + 1):
    if i == 1:
        num[i] = 1
        continue
    else:
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                num[i] = 1
                break

for i in range(a, b + 1):
    if num[i] == 0:
        print(i)
