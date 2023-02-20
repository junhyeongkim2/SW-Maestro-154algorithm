A, P = map(int, input().split())

alist = [A]
i = 0

while True:
    a = alist[i]
    temp = 0
    while a > 0:
        temp += ( a % 10 ) ** P
        a //= 10

    if temp in alist:  # 반복이 시작
        j = alist.index(temp)
        alist = alist[:j]
        break

    alist.append(temp)
    i += 1
    # if i == 30:
    #     break

print(len(alist))
