# 10815번 숫자 카드
# https://www.acmicpc.net/problem/10815
import copy

def binary(start, end):
    while start <= end:
        mid = (start+end)//2

        if cards[i] > sang[mid]: # 찾으려는 카드가 mid보다 큰 경우
            start = mid + 1
        elif cards[i] < sang[mid]:
            end = mid - 1
        else: # 같은 경우
            ans[cards[i]] += 1
            break

N = int(input())
cards = list(map(int, input().split()))

M = int(input())
sang = list(map(int, input().split()))
sang_copy = copy.deepcopy(sang)
ans = dict()
for s in sang:
    ans[s] = 0

sang.sort()
for i in range(len(cards)):

    # binary search
    binary(0, M-1)

for s in sang_copy:
    print(ans[s], end=' ')