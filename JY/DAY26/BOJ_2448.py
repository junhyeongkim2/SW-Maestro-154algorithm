import sys

input = sys.stdin.readline

n = int(input())

stars = [[' '] * 2 * n for _ in range(n)]


def recursion(i, j, size):
    if size == 3:
        stars[i][j] = '*'
        stars[i + 1][j - 1] = stars[i + 1][j + 1] = "*"
        for k in range(-2, 3):
            stars[i + 2][j - k] = "*"

    else:
        newSize = size // 2
        recursion(i, j, newSize)
        recursion(i + newSize, j - newSize, newSize)
        recursion(i + newSize, j + newSize, newSize)


recursion(0, n - 1, n)
for star in stars:
    print("".join(star))