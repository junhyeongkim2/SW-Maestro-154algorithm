from itertools import combinations

while True:
    S = list(map(int,input().split()))
    if S[0]==0:
        exit()

    del S[0]
    comb = combinations(S,6)
    for c in comb:
        print(*c)
    print()