# 1406번 에디터
# https://www.acmicpc.net/problem/1406
import sys
read = sys.stdin.readline

# list로 풀이(시간 복잡도가 조금 더 개선)

# 포인터 좌/우로 배열에 나누어 저장
left = list(read().strip()) # 커서 왼쪽 원소 저장
right = list() # 커서 오른쪽 원소 저장

for _ in range(int(read().strip())):
    t = read().split()
    if t[0]=='L':
        if left: # 커서 왼쪽이 비어있지 않은 경우
            right.append(left.pop())
    elif t[0]=='D':
        if right:
            left.append(right.pop())
    elif t[0]=='B':
        if left:
            left.pop()
    elif t[0]=='P':
        left.append(t[1])

for l in left:
    print(l,end='')
for r in reversed(right):
    print(r, end='')