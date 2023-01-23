from itertools import combinations
N, S = map(int, input().split(' '))
num = list(map(int, input().split(' ')))

cnt = 0
for i in range(N):
    comb = combinations(num, i+1)
    for c in comb:
        if sum(c)==S:
            cnt += 1
print(cnt)