# 11005 진법 변환 2
# https://www.acmicpc.net/problem/11005

N, B = map(int, input().split())
nums = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
result = list()

while N:
    result.append(nums[N%B])
    N//=B

for r in result[::-1]:
    print(r, end='')