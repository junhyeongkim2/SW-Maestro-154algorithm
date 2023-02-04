import sys

s = sys.stdin.readline().rstrip()
cnt = [-1] * 26

for i in range(len(s)):
    #문자열을 아스키코드로 바꾸고 97을 빼서 a일 땐 0
    ascindex = ord(s[i])-97
    if cnt[ascindex] == -1:
        cnt[ascindex] = i
    else:
        continue

print(*cnt)
