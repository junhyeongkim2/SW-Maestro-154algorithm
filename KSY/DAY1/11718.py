#방법 1
while True:
    try:
        line = input()
        print(line)
    except EOFError:
        break


#방법 2 #'\0'까지 출력 하는 것 같음
from sys import stdin
lines = stdin.readlines()
for line in lines:
    print(line)
