import sys

input = sys.stdin.readline

total , given = map(int, input().split())
table = [0] * (total)
for i in range(total):
    table[i] = int(input())
table.sort(reverse = True)

res = 0

for k in range(total):
    if table[k] <= given:
        res = res + (given//table[k])
        given = given % table[k]
        if given <= 0:
            break

       
print(res)


