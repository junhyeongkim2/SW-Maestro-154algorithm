# 11729번 하노이 탑 이동 순서
# https://www.acmicpc.net/problem/11729

global move
move = []

def hanoi(N, start, via, end):
    """

    :param N: 원판의 수
    :param start: 시작 기둥
    :param via: 중간 기둥
    :param end: 끝 기둥
    :return: 이동 횟수
    """
    if N <= 1: # 원판이 1개 있는 경우
        move.append((start, end))
        return 1

    cnt = 0
    cnt += hanoi(N-1, start, end, via) # N-1개의 원판을 보조 기둥에 모두 이동
    cnt += hanoi(1, start, via, end) # 가장 큰 원판을 끝 기둥에 이동
    cnt += hanoi(N-1, via, start, end) # N-1개의 원판을 끝 기둥에 이동

    return cnt

print(hanoi(int(input()), 1, 2, 3))
for f, t in move:
    print(f, t)