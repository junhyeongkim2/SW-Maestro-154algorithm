import sys
# import heapq
input = sys.stdin.readline

n = int(input())
meetingInfo = []
#풀이1
# heapq.heapify(meetingInfo) #list를 minheap으로
#
# for _ in range(n):
#     start, end = map(int, input().split())
#     heapq.heappush(meetingInfo, (end-start, start, end))
#
# meetingNow = heapq.heappop(meetingInfo)
#
# while len(meetingInfo) > 0:
#     meetingCandi = heapq.heappop(meetingInfo)
#     if meetingNow[0] > meetingCandi[0]:
#         meetingNow = meetingCandi
#     else:

#풀이2
for _ in range(n):
    start, end = map(int, input().split())
    meetingInfo.append((start, end))

meetingInfo.sort(key=lambda x: (x[1], x[0]))
now, result = 0, 0
for s, e in meetingInfo:
    if s >= now:
        now = e
        result += 1

print(result)
