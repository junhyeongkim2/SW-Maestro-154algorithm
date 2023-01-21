#2007년

DAY = ['MON','TUE','WED','THU','FRI','SAT','SUN']
DATE = [31,28,31,30,31,30,31,31,30,31,30,31]

x,y = map(int,input().split())
cal = 0
for i in range(1,x):
    cal += DATE[i-1]

cal += y

print(DAY[(cal%7)-1])
