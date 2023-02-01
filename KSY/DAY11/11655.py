s = input()
result = ""

for c in s:
    if c.isupper():
        if ord(c) <= 77:
            result += chr(ord(c) + 13)
        else:
            result += chr(ord(c) - 13)
    elif c.islower():
        if ord(c) <= 109:
            result += chr(ord(c) + 13)
        else:
            result += chr(ord(c) - 13)
    else:
        result += c

print(result)