import sys

input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    name, kr, en, math = input().split()
    arr.append([name, int(kr), int(en), int(math)])

print(arr)
#국어 (내림), 영어 (오름), 수학 (내림), 이름 (오름) 
arr.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in arr:
    print(i[0])
