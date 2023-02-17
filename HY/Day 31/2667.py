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