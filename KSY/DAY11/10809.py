n = input()
alphabet = [-1]*26

for i, a in enumerate(n):
    if alphabet[ord(a) - 97] == -1:
        alphabet[ord(a) - 97] = i

for i in alphabet:
    print(i, end=" ")