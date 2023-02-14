import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
broken = list(map(str, input().split()))
cnt = abs(100 - n) #리모컨을 눌러야하는 최대 개수

#for문을 통해 이동 채널로 가기 위한 방법을 확인
for i in range(1000000):
    for j in str(i): # 채널로 이동하기 위해 눌러야 하는 번호가 고장이 났는지 확인
        if j in broken: #만약 j가 고장난 버튼이면 pass
            break
        else:  #고장 안 났으면 cnt = min(기존 cnt, ((채널을 누른 개수) + (+/-를 누른 개수)) 
            cnt = min(cnt, len(str(i)) + abs(i - n))

print(cnt)