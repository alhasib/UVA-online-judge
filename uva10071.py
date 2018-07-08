while True:
    try:
        a,b = list(map(int,input().split()))
        c = (a * b)
        print(2*int(c))
    except EOFError:
        break