import sys
table = [list(sys.stdin.readline().split()) for _ in range(int(sys.stdin.readline()))]
for dot in sorted(table, key = lambda x : (int(x[1]), int(x[0]))):
    sys.stdout.write(str(int(dot[0]))+ " " + str(int(dot[1])) + "\n")