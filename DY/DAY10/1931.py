# 1931번 회의실 배정
# https://www.acmicpc.net/problem/1931
import sys
read = sys.stdin.readline
N = int(read().strip())
cnt = 0
prev = 0 # 이전 회의가 끝나는 시간
conf = [list(map(int, read().split())) for _ in range(N)]
conf.sort(key=lambda x:x[0])
conf.sort(key=lambda x:x[1])
# conf.sort(key=lambda x:(x[1], x[0]))와 동일
for s, e in conf:
    if prev <= s:
        cnt += 1
        prev = e
print(cnt)