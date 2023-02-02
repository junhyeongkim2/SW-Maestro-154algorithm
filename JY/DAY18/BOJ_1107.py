import sys

input = sys.stdin.readline

goal = int(input())

total = int(input())

c = list(map(int, input().split()))

min_count = abs(100 - goal)  


for number in range(1000001):
    number = str(number)
    for k in range(len(number)):
        if int(number[k]) in c:
            break
        elif k == len(number)-1:
            min_count = min(min_count, abs(goal-int(number))+len(number))
        
print(min_count)
