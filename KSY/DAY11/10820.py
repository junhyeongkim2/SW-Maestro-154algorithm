import sys
input = sys.stdin.readline

while True:
    alist = [0] * 4
    n = input().rstrip('\n')

    if not n:
        break
    for i in n:
        if i.isspace():  # 공백 #.isspace() 변환 가능
            alist[3] += 1
        elif i.isupper():  # 대문자 #.isupper()
            alist[1] += 1
        elif i.islower():  # 소문자 #islower()
            alist[0] += 1
        elif i.isdigit():  # 48 ~ 57 : 숫자 #.isdigit()
            alist[2] += 1

    print(alist[0], alist[1], alist[2], alist[3])
