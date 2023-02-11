import sys

input = sys.stdin.readline

# [point] 10진수로 변경 후 처리, 입력 숫자의 의미 파악

A, B = map(int, input().split())
n = int(input())
numbers = list(input().split())

# 10진수로 변경
base10 = 0
for i, num in enumerate(reversed(numbers)):
    base10 += (A**i)*int(num)  # 10이 아닌 A..!

result = []
while base10 != 0:
    result.append(str(base10 % B))
    base10 //= B

result.reverse()
print(' '.join(result))

