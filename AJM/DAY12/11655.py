#11655 ROT13

string = str(input())
answer = ""
for s in string:
    if s.isupper():
        ch = ord(s)+13
        if ch > 90:
            ch -= 26
        answer += chr(ch)
    elif s.islower():
        ch = ord(s)+13
        if ch>122:
            ch -= 26
        answer += chr(ch)
    else:
        answer += s
print(answer)
