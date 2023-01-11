# 10820번 문자열 분석
# https://www.acmicpc.net/problem/10820

# 아스키코드 값으로 풀이
import sys
read = sys.stdin.readline

while True:
    try: # 입력이 안 되는 경우 EOFError 발생
        str = input()
    except:
        exit()

    result = [0]*4
    for s in str:
        asc = ord(s)
        if 97<=asc<=122:
            result[0]+=1
        elif 65<=asc<=90:
            result[1] += 1
        elif 48<=asc<=57:
            result[2]+=1
        else:
            result[3]+=1
    print(*result)