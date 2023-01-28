import sys

input= sys.stdin.readline

total, N = map(int, input().split())

tree = list(map(int, input().split()))

start = 0
end = max(tree)

while start <= end:
    mid = (start + end) // 2
    res = 0
    for i in range(total):
        if tree[i] >= mid:
            res = res + (tree[i] - mid)
    if res >= N:
        start = mid +1
    else:
        end = mid -1
    
print(end)
