import sys
read = sys.stdin.readline

while True:
    try:
        a, b = map(int, read().split())
        print(a+b)
    except:
        break