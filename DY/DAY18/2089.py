# 2089번 -2진수
# https://www.acmicpc.net/problem/2089

N = int(input().strip())

if N==0:
    print(0)
else:
    result = ''
    while N!=0:
        if N%(-2)==0: # 나머지가 없는 경우
            result += '0'
            N = N//(-2)
        else: # 나머지가 있는 경우
            result += '1'
            N = N//(-2)+1

    for i in result[::-1]:
        print(i,end='')