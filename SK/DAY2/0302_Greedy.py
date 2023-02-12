'''
큰 수의 법칙
''' 

# Input
n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))

# Define variables
result = 0

# Algorithm
numbers.sort()

first = numbers[-1]
second = numbers[-2]

routine = m // k+1
result = (m - routine) * first + second * routine

# Output
print(result)