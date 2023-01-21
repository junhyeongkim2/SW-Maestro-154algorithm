# 10808번 알파벳 개수
# https://www.acmicpc.net/problem/10808

str = input()
alpha = [0]*26
for s in str:
    alpha[ord(s)-97] += 1
print(*alpha)