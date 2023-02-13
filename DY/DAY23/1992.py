import sys
read = sys.stdin.readline

def quad(N, x, y):
    result = True
    for r in range(N):
        for c in range(N):
            if graph[x][y] != graph[x + r][y + c]:
                result = False
                break
        if not result:
            break

    if result:
        print(graph[x][y], end='')
        return 0

    N //= 2
    print('(', end='')
    for r in range(2):
        for c in range(2):
            quad(N, x + N * r, y + N * c)
    print(')', end='')


if __name__ == '__main__':
    N = int(read().strip())
    graph = [list(map(int, read().strip())) for _ in range(N)]
    quad(N, 0, 0)