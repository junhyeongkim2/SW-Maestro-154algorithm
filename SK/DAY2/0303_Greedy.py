'''
숫자 카드 게임
'''

# Input
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# Define variables
result = 0

# Algorithm
for i in range(n):
    tmp_min = min(arr[i])
    result = max(tmp_min, result)

# Output
print(result)