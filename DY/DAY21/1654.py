import sys
K, N = map(int, sys.stdin.readline().split())
lan = [int(sys.stdin.readline()) for _ in range(K)]

start, end = 1, max(lan)
while start <= end:
    mid = (start+end) // 2
    line = 0
    for i in lan:
        line += i//mid

    if line >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)