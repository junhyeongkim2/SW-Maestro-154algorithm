day=['SUN','MON','TUE','WED','THU','FRI','SAT']
date=[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m,d=map(int, input().split())
n=0

for i in range(m):
	n+=date[i]
n+=d
n%=7
print(day[n])