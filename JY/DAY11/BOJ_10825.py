import sys

table = [list(sys.stdin.readline().split()) for _ in range(int(sys.stdin.readline()))]
for name in sorted(table, key = lambda x : (-int(x[1]),int(x[2]), -int(x[3]), x[0] )):
    sys.stdout.write(str(name[0])+"\n")