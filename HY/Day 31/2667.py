"""
<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 
철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 
여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 
대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 
지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 
출력하는 프로그램을 작성하시오.

알고리즘

"""
#단지 출력하기 dfs
import sys
sys.stdin.readline
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input())

#단지 지도 만들기
maps = []
for i in range(n):
    maps.append(list(map(int, input().strip())))

def dfs(x,y):
    global home #한 단지에 집이 몇개인지 셀 변수
    if x < 0 or y < 0 or x >= n or y >= n: #범위를 벗어나면 fasle
        return False
#만약 집이 있으면
    if maps[x][y] == 1:
        home += 1 #집의 수 1개 추가
        maps[x][y] = 0 #숫자를 세고 0으로 집을 없앰
        dfs(x-1,y) #상하좌우 재귀
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True #True 반환
    return False

nums = [] # 각 단지의 집의 수를 담는 리스트
home = 0

for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            nums.append(home) #리스트에 집의 수 출력
            home = 0 #한 단지에 있는 집의 수를 다시 0으로 초기화
nums.sort() #오름차순
#내림차순은 nums = sorted(nums, key= lambda -x:0)
print(len(nums)) #c총 집의 수 출력
for i in nums:
  print(i)