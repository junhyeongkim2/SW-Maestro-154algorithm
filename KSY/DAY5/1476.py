E, S, M = map(int, input().split())
result, e, s, m = 1, 1, 1, 1

while True:
    if e == E and m == M and s == S:
        break
    e += 1
    m += 1
    s += 1
    result += 1
    if e == 16:
        e = 1
    if m == 20:
        m = 1
    if s == 29:
        s = 1

print(result)
