m, d = map(int, input().split())
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
day = 0

for i in range(m-1):
    day += month[i]
print(week[(d + day) % 7 - 1])
