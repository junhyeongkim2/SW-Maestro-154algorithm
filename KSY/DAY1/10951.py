#방법 1
while True:
    try:
        a, b = list(map(int, input().split()))
        print(a + b)
    except EOFError:
        break

#방법 2
from sys import stdin
lines = stdin.readlines()
for line in lines:
    a, b = map(int, line.split())
    print(a + b)
