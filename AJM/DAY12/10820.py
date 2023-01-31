#10820 문자열 분석
import sys

while(True):
    string = str(sys.stdin.readline().rstrip('\n'))

    if not string:
        break
    
    l,u,n,b = 0,0,0,0
    
    for s in string:
        if ord(s) == 32:
            b += 1
        elif ord(s)>96:
            l += 1
        elif ord(s)>64 and ord(s)<97:
            u += 1
        elif ord(s)<65:
            n += 1
            
    print(l,u,n,b)


"""
문자열에서 소문자 판별
s.islower()
대문자 판별
s.isupper()
숫자 판별
s.isdigit()
공백판별
s.isspace()
"""