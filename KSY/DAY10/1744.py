import sys
input = sys.stdin.readline

n = int(input())
positive = []
negative = []
result = 0

for i in range(n):
    number = int(input())
    if number > 1:
        positive.append(number)
    elif number == 1:
        result += 1
    else:
        negative.append(number)

positive.sort(reverse=True) #큰 수부터
negative.sort() #작은 수 부터 ex. -3 -2 -1 0

for i in range(0, len(positive), 2):
    if i < len(positive) - 1:
        result += positive[i]*positive[i+1]
    else:
        result += positive[i]

for j in range(0, len(negative), 2):
    if j < len(negative) - 1:
        result += negative[j]*negative[j+1]
    else:
        result += negative[j]

print(result)
