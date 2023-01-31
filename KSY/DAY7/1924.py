weekday = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
x, y = map(int, input().split())
day = 0

for m in range(x-1):
    day += month[m]
day += y
print(weekday[day % 7])