import sys
list = []

for i in range(int(input())):
    list.append(int(sys.stdin.readline()))

for i in sorted(list):
    print(list[i])