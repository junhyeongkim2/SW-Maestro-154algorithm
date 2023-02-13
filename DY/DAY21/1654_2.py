import sys
read = sys.stdin.readline

N, K = map(int, read().split())
wire = [int(read().strip()) for _ in range(N)]

start, end = 1, max(wire)

while start <= end:
    ans = 0
    mid = (start+end)//2
    for w in wire:
        ans += w//mid

    if ans >= K:
        start = mid+1
    else:
        end = mid-1
print(end)