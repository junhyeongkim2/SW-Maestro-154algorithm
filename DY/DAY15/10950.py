import sys
read = sys.stdin.readline

for _ in range(int(read().strip())):
    print(sum(list(map(int, read().split()))))