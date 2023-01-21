# back Tracking을 이용하여 풀이

def dfs(cur):
    if len(result)==6:
        print(' '.join(map(str,result)))
        return

    for i in range(cur+1, N):
        if S[i] not in result:
            result.append(S[i])
            dfs(i)
            result.pop()

while True:
    S = list(map(int,input().split()))
    if S[0]==0:
        exit()
    N = S[0]
    del S[0]

    S.sort()
    result = []
    dfs(-1)
    print()

