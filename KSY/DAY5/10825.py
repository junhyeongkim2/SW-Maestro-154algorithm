from sys import stdin
n = int(stdin.readline())
peopleList = []

for _ in range(n):
    name, ko, en, ma = stdin.readline().split()
    peopleList.append((name, int(ko), int(en), int(ma)))

peopleList.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for p in peopleList:
    print(p[0])