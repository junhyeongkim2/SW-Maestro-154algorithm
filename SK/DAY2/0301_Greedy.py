'''
거스름돈
'''

# Input
n = int(input())

# Define variables
count = 0
coins = [500, 100, 50, 10]

# Algorithm
for coin in coins:
    count += (n // coin)
    n = n % coin

# Output
print(count)