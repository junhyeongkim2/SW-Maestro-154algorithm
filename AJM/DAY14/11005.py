#11005 진법 변환 2

s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n,b = map(int,input().split())
answer = ''
while(n):
    answer += str(s[n % b])
    n //= b

print(answer[::-1])
    