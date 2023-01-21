# 10799번 쇠막대기
# https://www.acmicpc.net/problem/10799

from collections import deque

stack = deque()
stick = input()
ans = 0

for i in range(len(stick)):
    if stick[i] == '(':
        stack.append('(')
    elif stick[i-1] == '(': # 레이저를 만난 경우, 잘린 막대기를 추가(잘린 막대기의 개수는 스택의 크기와 동일)
        stack.pop() # 레이저의 '(' 삭제
        ans += len(stack)
    else: # 막대의 끝
        ans += 1
        stack.pop()
print(ans)

'''
from collections import deque

stack = deque(input())

ans = 0 # 최종 개수
stick = 0 # for문 내 stack 개수

while stack:
    prev = stack.pop() # top에 있는 값
    if prev == ')':
        if stack[-1] == '(': # 레이저인 경우
            ans += stick
            stack.pop() # 레이저의 '('를 제거
        else: # 쇠막대기인 경우
            stick += 1
    else: # '('인 경우
        ans += 1
        stick -= 1

print(ans)
'''