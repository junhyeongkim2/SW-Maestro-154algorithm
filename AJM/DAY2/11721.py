#열개씩 끊어 출력하기 

s = input()

for i in range((len(s)//10)+1):
    print(s[i*10:(i*10)+10])
