from sys import stdin
n = int(stdin.readline())
coordinates = []

for _ in range(n):
    x, y = map(int, stdin.readline().split())
    coordinates.append((x, y))

coordinates.sort(key=lambda x: (x[0], x[1]))

for x, y in coordinates:
    print(x, y)