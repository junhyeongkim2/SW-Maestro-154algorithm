import sys
input = sys.stdin.readline

N, Need = map(int, input().split())
tree = list(map(int, input().split()))


start, end = 1, max(tree)  # 시작점, 끝점

while start <= end:
    sum = 0
    mid = (start + end) // 2

    # 나무를 잘라서 합치는 과정
    for i in tree:
        if i - mid > 0: #자른 수가 음수가 아니라면
            sum = sum + (i - mid)
        else:
            continue
        if sum > Need: #절단된 나무를 더할 때 이미 Need를 넘으면 
            break
    if sum >= Need: 
        start = mid + 1
    else:
        end = mid - 1
print(end)
