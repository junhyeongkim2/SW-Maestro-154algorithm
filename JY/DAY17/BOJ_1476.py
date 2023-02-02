E, S, M = map(int,input().split())

Y = 1

while True:
  if (Y-E) % 15 == 0 and (Y-S) % 28 == 0 and (Y-M) % 19 == 0 :
    break
  Y += 1

print(Y)