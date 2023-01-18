a = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]  # 요일을 담은 list a
# 각 월별 총 일수를 담은 list b[0]은 1월 b[1]은 2월 ..... b[11]은 12월의 총 일수이다
b = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = 0

m, d = map(int, input().split())  # 입력값 받기 m-월 d-일

for i in range(0, m-1):  # 입력한 월 전까지의 총 일수를 다 더하기 예를 들어, 1월이면 아무것도 더하지 않고, 3월이면 1월~2월까지의 일수를 더한다
    day += b[i]


answer = (day + d) % 7  # 요일은 day + 입력 일수 중 7로 나눈 나머지이다.

print(a[answer])
