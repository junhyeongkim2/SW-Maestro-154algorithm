import sys
input = sys.stdin.readline

N = int(input())
inven = list(map(int, input().split()))
M = int(input())
card = list(map(int, input().split()))

cnt = {} # 횟수를 저장하는 dictionary
for i in inven: # inven에 존재하는 카드를 하나씩 순회하면서 dict에 횟수 저장
    if i in cnt: # 앞에서 이미 저장한 적이 있으면 +1
        cnt[i] += 1
    else: # 처음 나오는 카드면 1로 초기화
        cnt[i] = 1

for c in card:
    print(cnt.get(c, 0), end=' ') # cnt에 c가 존재하면 해당 value를, 없으면 0을 출력하도록 함