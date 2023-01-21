E,S,M = map(int, input().split())
year = 0
while True:
    if year%15==E-1 and year%28==S-1 and year%19==M-1:
        break
    year += 1
print(year+1)