n, m = map(int, input().split())

if n==1:
  print(1)
elif n==2:
  if m>=7:
    print(4)
  else:
    print(int((m+1)/2))
else:
  if m<=4:
    print(m)
  elif m==5or m==6:
    print(4)
  else:
    print(m-2)
