import sys
input = sys.stdin.readline

N = int(input())

def star(num):
    if num == 3:
        return ['***', '* *', '***']
    arr = star(num // 3)
    res = []
    for i in arr:
        res.append(i * 3)
    for i in arr:
        res.append(i + " "*(num//3) + i)
    for i in arr:
        res.append(i*3)
    return res

print("\n".join(star(N)))




