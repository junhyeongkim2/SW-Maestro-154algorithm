import sys
read = sys.stdin.readline

def paper(n, r, c):
    global cnt

    result = True
    for i in range(n):
        for j in range(n):
            if graph[r][c] != graph[r+i][c+j]:
                result = False
        if not result:
            break

    if result:
        cnt[graph[r][c]] += 1
        return 0

    n //= 3
    for i in range(3):
        for j in range(3):
            paper(n, r+n*i, c+n*j)

if __name__ == '__main__':
    N = int(read().strip())
    cnt = {-1:0, 0:0, 1:0}

    graph = [list(map(int, read().split())) for _ in range(N)]
    paper(N, 0, 0)
    for k, v in cnt.items():
        print(v)