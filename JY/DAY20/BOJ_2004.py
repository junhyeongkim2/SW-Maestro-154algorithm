import sys

input = sys.stdin.readline

A, B = map(int, input().split())

r = 1
l = 1

def countfive(num):
    cnt = 0
    while num >= 5:
        cnt += num//5
        num = num // 5
    return cnt

def counttwo(num):
    cnt = 0
    while num >= 2:
        cnt += num // 2
        num = num//2
    return cnt

fivenum = countfive(A) - countfive(A-B) - countfive(B)
twonum = counttwo(A) - counttwo(A-B) - counttwo(B)

print(min(fivenum, twonum))
