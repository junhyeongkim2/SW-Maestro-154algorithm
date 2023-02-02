# 2331번 반복수열
# https://www.acmicpc.net/problem/2331

A, P = map(int, input().split())
seq = dict()
cnt = 1
seq[A] = cnt
while True:
    num = 0
    while A:
        num += (A%10)**P
        A //= 10
    A = num
    cnt += 1
    try:
        if seq[A]:
            print(seq[A]-1)
            break
    except:
        seq[A] = cnt