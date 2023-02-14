import sys
input = sys.stdin.readline

E, S, M = map(int, input().split())
cnt = 0
while True:
    if (cnt-E) % 15 == 0 and (cnt-S) % 28 == 0 and (cnt-M) % 15 == 0:
        break
    cnt += 1

print(cnt)
