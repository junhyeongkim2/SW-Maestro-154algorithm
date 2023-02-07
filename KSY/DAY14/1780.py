import sys
input = sys.stdin.readline
answer = [0, 0, 0]  # -1, 0, 1의 개수

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
#또는 board = [list(map(int, input().split())) for _ in range(N)]

def loop(x, y, N):  # board의 시작위치(x, y), 원소 개수

    # board 모두 돌면서 다른 수가 있는지 확인
    number = board[x][y]
    for i in range(N):
        for j in range(N):
            if number != board[x+i][y+j]: #다른 수가 있다면
                for k in range(3): #NxN을 각 3등분 하는 것이므로!!
                    for l in range(3):
                        loop(x + N * k // 3, y + N * l // 3, N // 3)
                return

    answer[board[x][y]] += 1

loop(0, 0, N)

print(answer[-1], answer[0], answer[1])