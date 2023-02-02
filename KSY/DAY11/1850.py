import math
# answers = []
# for i in range(1, 9):
#     answers.append(int('1'*i))

a, b = map(int, input().split())


print('1'*math.gcd(a, b))
