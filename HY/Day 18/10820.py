import sys

while True:
    try:
        cntlow, cntup, cntnumber, cntzero = 0, 0, 0, 0
        n = input()
        if not n:
            break

        for i in n:
            if i.islower():
                cntlow += 1
            if i.isupper():
                cntup += 1
            if i.isdigit():
                cntnumber += 1
            if i == " ":
                cntzero += 1
        print(cntlow, cntup, cntnumber, cntzero)
    except EOFError:
        break
