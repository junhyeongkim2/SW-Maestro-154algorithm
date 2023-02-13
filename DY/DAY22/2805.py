import sys
read = sys.stdin.readline

def binary_search(arr, start, end):
    while start <= end:
        mid = (start + end) // 2
        ans = 0
        for t in tree:
            if t>mid:
                ans += t - mid

        if ans >= M:  # 클 경우
            start = mid + 1
        elif ans < M:  # 작을 경우
            end = mid - 1
    return end

N, M = map(int, read().split())
tree = list(map(int, read().split()))

end = binary_search(tree, 0, max(tree))
print(end)