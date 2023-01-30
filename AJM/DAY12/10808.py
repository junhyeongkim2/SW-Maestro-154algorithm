"""
ord(문자) 는 유니코드 정수를 반환함.
ex. ord('a') = 97
chr(정수) 는 유니코드 문자를 반환함.
ex. chr(97) = a
"""
#10808 알파벳 개수
s = str(input())
al = [0] * 26
for i in s:
    al[ord(i)-97] += 1

for i in al:
    print(i,end=" ")
#print(*al) 도 가능