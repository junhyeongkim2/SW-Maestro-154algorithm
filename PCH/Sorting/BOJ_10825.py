import sys
input = sys.stdin.readline

N = int(input())
box = []
for i in range(N): 
  name, kor, eng, math = input().split()
  box.append([name, int(kor), int(eng), int(math)])

# 조건 여러개, 순서 바꿀 때는 - 붙이기
box.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

for student in box:
  print(student[0])