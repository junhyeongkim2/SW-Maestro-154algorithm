# 1373 2진수 8진수
# https://www.acmicpc.net/problem/1373

N=input().strip()
result = []

st = len(N)%3
if st != 0: result.append(int(N[:st], 2))
for i in range(st, len(N), 3):
    result.append(int(N[i:i+3], 2))

for r in result:
    print(r, end='')