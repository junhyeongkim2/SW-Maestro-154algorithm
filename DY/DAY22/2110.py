# 2110번 공유기 설치
# https://www.acmicpc.net/problem/2110
import sys
read = sys.stdin.readline

def binary_search(start, end):
    global C

    while start <= end:
        mid = (start + end) // 2
        cnt = 1
        prev = pos[0]
        for i in range(1, len(pos)):
            if pos[i] - prev >= mid:
                prev = pos[i]
                cnt += 1

        if cnt >= C:  # 공유기가 더 많이 설치된 경우
            start = mid + 1
        elif cnt < C:  # 공유기가 덜 설치된 경우
            end = mid - 1

    print(end)

N, C  = map(int, read().split())
pos = [int(read().strip()) for _ in range(N)]

pos.sort()
binary_search(1, pos[-1]-pos[0])