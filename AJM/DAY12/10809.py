#10809 알파벳 찾기
s = str(input())
al = [-1] * 26
for i,s in enumerate(s):
    if al[ord(s)-97] == -1:
        al[ord(s)-97] = i

print(*al)

