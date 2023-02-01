n = input()
alphabet = [0]*26

for a in n:
    alphabet[ord(a) - 97] += 1

for a in alphabet:
    print(a, end=" ")