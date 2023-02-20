"""
숨바꼭질 1697 골드 4
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 
동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 
만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 
구하는 프로그램을 작성하시오.

최단시간을 구하는 문제 = 그래프 문제
이동 방향은 X - 1, X + 1, 2 x X 로 총 3가지로 노드가 펼쳐진다
"""
import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())  # 수빈이 위치, 동생위치
limit = 222222
time = [0] * 222223 #시간을 담을 변수 limit + 1만큼 생성

def bfs(v):
    q = deque()
    q.append(v)
    while q:
        now = q.popleft()
        d = [now-1, now+1, now*2] #이동수
        if now == k:  # 동생 만나면
            print(time[now])  #정답 걸린 시간 출력
            break
        for i in d:  # now가 5일 경우, 4,6,10 // 가려는 위치가 0보다 크고 리미트보다 작으면서 방문하지 않았을 때
            if 0 <= i <= limit and time[i] == 0:
                time[i] = time[now] + 1  # 지금까지 걸린 시간 +1
                q.append(i) #큐에 넣기 q=deque([4,6,"10"])

bfs(n)
