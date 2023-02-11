'''
시각
'''

# Input
n = int(input())

# Define variables
count = 0

# Algorithm
for hour in range(n+1):
    for minute in range(60):
        for second in range(60):
            if '3' in str(hour)+str(minute)+str(second):
                count += 1

# Output
print(count)