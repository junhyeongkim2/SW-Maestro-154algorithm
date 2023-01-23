import sys
read = sys.stdin.readline

for i in range(int(read().strip())):
    a, b = map(int, read().split())
    print(f'Case #{i+1}: {a + b}')