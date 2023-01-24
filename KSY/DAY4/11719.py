from sys import stdin

for sentence in stdin:
    try:
        print(sentence, end='')
    except EOFError:
        break
