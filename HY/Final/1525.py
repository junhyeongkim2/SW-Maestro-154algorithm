import sys
from collections import deque
input = sys.stdin.readline

purzle = ""
#퍼즐 담아오는 함수
for _ in range(3):
  inpurzle = input().strip()
  inpurzle = inpurzle.replace(" ", "")
  purzle += inpurzle

#카운트를 담을 딕셔너리
cnt = {}
cnt[purzle] = 0
#위아래 상하좌우 탐색
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
  q = deque()
  q.append(purzle)

  while q:
    cur = q.popleft()
    if cur == "123456780":
      return cnt[cur]
    
    zeroindx = str(cur).find("0")
    x = zeroindx // 3
    y = zeroindx % 3
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if 0 <= nx < 3 and 0 <= ny < 3:
        nextzero = nx * 3 + ny
        curlist = list(cur)
        curlist[nextzero], curlist[zeroindx] = curlist[zeroindx], curlist[nextzero]
        curlist = "".join(curlist)

        if not cnt.get(curlist):
          q.append(curlist)
          cnt[curlist] = cnt[cur] + 1

result = bfs()
if result == None:
  print(-1)
else:
  print(result)