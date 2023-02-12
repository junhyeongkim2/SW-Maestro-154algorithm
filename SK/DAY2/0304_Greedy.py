'''
1이 될 때까지
'''

# Input
n, k = map(int, input().split())

# Define variables
count_div, count_sub = 0, 0

# Algorithm
while n > 1:
    quot, remain = divmod(n, k)
    if remain == 0:
        n = quot
        count_div += 1
    elif n > k:
        n = n - remain
        count_sub += remain
    else:
        n = n - (remain - 1)
        count_sub += (remain - 1)

# Output
print(count_div + count_sub)