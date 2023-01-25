import sys
list = [list(sys.stdin.readline().split()) for _ in range(int(input()))]
for i in sorted(list, key = lambda  x : int(x[0])):
    print(i[0] + " " + i[1])