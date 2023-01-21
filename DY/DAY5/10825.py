# 10825 국영수
# https://www.acmicpc.net/problem/10825
import sys
read = sys.stdin.readline

stud = []
for _ in range(int(read().strip())):
    stud.append(read().split())
stud.sort(key=lambda x: x[0]) # 이름이 증가하는 순서
stud.sort(key=lambda x: int(x[3]), reverse=True) # 수학이 감소하는 순서
stud.sort(key=lambda x: int(x[2])) # 영어가 증가하는 순서
stud.sort(key=lambda x: int(x[1]), reverse=True)

for s in stud:
    print(s[0])