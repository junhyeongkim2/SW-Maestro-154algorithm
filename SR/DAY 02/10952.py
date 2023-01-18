while True:
    try:
        a,b = map(int, input().split())
        c = a + b
        if c == 0:
             False
        else:
            print(a + b)
    except:
        break