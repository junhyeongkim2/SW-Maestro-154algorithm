n = int(input())
meeting = []
for i in range(n):
  n, m = map(int, input().split())
  meeting.append([n,m])
 #종료시간 오름차순 먼저 하고 시작시간을 오름차순
meeting.sort(key=lambda x: (x[1], x[0]))
print(meeting)

#끝나는 시간을 담을 변수
curEndtime = 0
result = 0


# 현재 구조 i번째미팅[시작시간][끝나는시간]
#          meeting[i[0][1], i+1[0][1],i+2[0][1] ] 
for i in meeting :
    #현재 끝나는 시간이 시작시간보다 크면
  if curEndtime <= i[0]:
    #끝나는 시간을 바꿈 
    curEndtime = i[1]
    #회의 횟수를 1 추가
    result += 1
print(result)
    