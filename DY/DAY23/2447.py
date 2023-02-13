# 2447번 별 찍기 - 10
# https://www.acmicpc.net/problem/2447

def draw_star(n):
    if n == 1:
        return '*'

    stars = draw_star(n//3) # 이전 단계의 별의 패턴을 저장(재귀)
    result = []

    for s in stars:
        result.append(s * 3)

    for s in stars:
        result.append(s + ' ' * (n//3) + s)

    for s in stars:
        result.append(s * 3)

    return result

ans = draw_star(int(input()))
for a in ans:
    print(a)



"""
def draw_star(n): # 배열(ans)에 ***를 저장
    if n == 1:
        return '*'

    star = draw_star(n//3)
    result = []
    for i in range(n):
        if (i // (n//3)) == 1:
            result.append(star[i%(n//3)] + ' ' * (n//3) + star[i%(n//3)])
            continue
        result.append(star[i%(n//3)] * 3)
    return result

ans = draw_star(int(input()))
for a in ans:
    print(a)
"""