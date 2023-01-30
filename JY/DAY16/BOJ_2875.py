import sys

input = sys.stdin.readline
F, M, I = map(int, input().split())

res = F // 2
remain = F %2
while True:
    if res == 0:
        print(0)
        break
    if M >= res:
        if (M - res) + remain >= I:
            print(res)
            break
        else:
            res = res -1
            remain += 2
    else:
        res = res -1
        remain += 2       
