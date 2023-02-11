# Input
n = int(input())

# Define variables
input_list = []

# Algorithm
for _ in range(n):
    num = int(input())
    input_list.append(num)

input_list.sort()

# Output
for i in range(n):
    print(input_list[i])
