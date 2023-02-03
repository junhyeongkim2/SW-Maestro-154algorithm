import sys
n = sys.stdin.readline().rstrip("\n")
result = ""

for i in n:
    if i >= "a" and i <= "z":
        i = ord(i)+13
        if i > 122:
            i = i-122+96
        result += chr(i)
    elif i >= "A" and i <= "Z":
        i = ord(i)+13
        if i > 90:
            i = i-90+64
        result += chr(i)
    else:
        result += i

print(result)
