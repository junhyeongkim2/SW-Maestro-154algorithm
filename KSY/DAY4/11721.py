words = input()
x = 0
while len(words[x:x+10]) == 10:
    print(words[x:x+10])
    x += 10
else:
    print(words[x:])
