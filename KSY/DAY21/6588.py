import sys

# input = sys.stdin.readline
def solution():
    # 소수 구하기
    alist = [False, False] + [True] * 1000000

    for i in range(2, 1001):
        if alist[i]:
            for j in range(i + i, 1000001, i):
                alist[j] = False

    while True:
        n = int(sys.stdin.readline())
        if n == 0: break

        a = 0
        b = n
        for _ in range(1000000):
            if alist[a] and alist[b]:
                print(f"{n} = {a} + {b}")
                break
            a += 1
            b -= 1
        else:
            print("Goldbach's conjecture is wrong.")

solution()