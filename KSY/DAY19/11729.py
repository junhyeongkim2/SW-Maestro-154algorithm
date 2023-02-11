n = int(input())
cource = []
def hanoi(From, To, Num):  # From : 현재 위치, To : 갈 위치
    if Num == 1:
        cource.append((From, To))
        return 1

    count = hanoi(From, 6-From-To, Num-1)  # From + End + ??? = 6
    cource.append((From, To))
    count += hanoi(6-From-To, To, Num-1)
    return count + 1


print(hanoi(1, 3, n))
for c in cource:
    print(c[0], c[1])