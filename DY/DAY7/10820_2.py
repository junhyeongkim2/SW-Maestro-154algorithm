# 10820번 문자열 분석
# https://www.acmicpc.net/problem/10820

# 각 인자를 구분하는 함수로 풀이
import sys
read = sys.stdin.readline

while True:
    try: # 입력이 안 되는 경우 EOFError 발생
        str = input()
    except:
        exit()

    result = [0]*4
    for s in str:
        if s.islower(): # 소문자
            result[0]+=1
        elif s.isupper(): # 대문자
            result[1] += 1
        elif s.isdigit(): # 숫자
            result[2]+=1
        elif s.isspace(): # 공백
            result[3]+=1
    print(*result)