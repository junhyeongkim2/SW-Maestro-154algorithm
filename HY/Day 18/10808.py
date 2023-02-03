import sys

s = sys.stdin.readline().rstrip()
cnt = [0] * 26  # 알파벳은 26개니까 26개의 cnt

# 아스키코드로 바꾸고 a의 아스키코드가 97이므로 (아스키코드 - 97)을 뺀 값을 cnt의 인덱스로 넣어준다.
for i in s:
    cnt[ord(i)-97] += 1

# 하나씩 출력
for i in cnt:
    print(i, end=" ")
