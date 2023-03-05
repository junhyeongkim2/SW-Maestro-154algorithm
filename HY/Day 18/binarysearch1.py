import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tteok = list(map(int, input().split()))

# 이진탐색 시작/끝점 설정
start = 0
end = max(tteok)

# 이진 탐색 수행(반복)
result = 0
while (start <= end):
    total = 0  # 잘랐을 때 떡의 양
    # 중간점
    mid = (start + end) // 2
    
    for i in tteok:
        if i > mid:  # 떡의 값이 중간점보다 크면
            total += (i - mid)  # 잘랐을 때의 떡의 합 = 떡 - 중간점
    if total < m:  # 잘랐을 때의 합이 고객이 원하는 것보다 작으면
        end = mid - 1  # 끝점을 왼쪽으로 이동

    else:  # 잘랐을 때의 합이가 고객이 원하는 것보다 크면
        result = mid  # 일단 기록
        start = mid + 1  # 중간점을 오른쪽으로 이동
print(result)
