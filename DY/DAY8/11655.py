# 11655번 ROT13
# https://www.acmicpc.net/problem/11655

for s in input():
    if s.islower(): # 소문자
        ch = ord(s)+13
        if ch > 122: # 소문자 범위를 벗어난 경우
            ch -= 26
        print(chr(ch), end='')
    elif s.isupper(): # 대문자
        ch = ord(s)+13
        if ch > 90: # 대문자 범위를 벗어난 경우
            ch -= 26
        print(chr(ch), end='')
    else: # 알파벳이 아닌 경우
        print(s, end='')