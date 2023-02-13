# 10815번 숫자 카드
# https://www.acmicpc.net/problem/10815

def binary(start, end):
    while start <= end:
        mid = (start+end)//2

        if cards[i] > sang[mid]: # 찾으려는 카드가 mid보다 큰 경우
            start = mid + 1
        elif cards[i] < sang[mid]:
            end = mid - 1
        else: # 같은 경우
            ans[i] = 1
            break

N = int(input())
sang = list(map(int, input().split()))

M = int(input())
cards = list(map(int, input().split()))

ans = [0] * M
sang.sort()
for i in range(len(cards)):

    # binary search
    binary(0, N-1)

print(*ans)