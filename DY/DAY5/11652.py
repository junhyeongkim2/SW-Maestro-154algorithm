# 11652번 카드
# https://www.acmicpc.net/problem/11652
import sys
import math
read = sys.stdin.readline

card_li = [int(read().strip()) for _ in range(int(read().strip()))]
card = dict()
for c in card_li:
    try:
        card[c] += 1
    except:
        card[c] = 1

ans = [math.inf, -math.inf]
for k, v in card.items():
    if ans[1] < v: # 기존 게 작은 경우
        ans[0] = k
        ans[1] = v
    elif ans[1] == v: # 같은 경우
        ans[0] = min(ans[0], k)

print(ans[0])