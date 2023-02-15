"""
수들의 합 2 완전탐색 / 투포인터
투포인터를 사용하여 시작점과 끝점을 arr에 하나씩 늘려가며 확인함 
시작점~끝점의 합이 m과 같으면 cnt +=1, 끝점을 뒤로 보냄
시작점~끝점의 합이 m보다 작으면 시작점+=1
시작점~끝점의 합이 m보다 크면 끝점 +=1
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
cnt, start, end = 0, 0, 1 #카운트, 시작점, 끝점 초기화

while (start <= end and end <= n):
    summ = sum(arr[start:end]) #투포인터로 배열의 합 
    if summ == m: #합이 m과 같으면
        cnt += 1 #카운트
        end += 1 #끝점을 뒤로 이동
    elif summ < m: #합이 작으면 끝점을 한칸 이동
        end += 1
    elif summ > m: #합이 크면 시작점을 한 칸 이동
        start += 1
print(cnt)
