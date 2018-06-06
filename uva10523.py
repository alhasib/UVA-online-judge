while True:
    try:

        a,b = list(map(int,input().split()))
        s = 0
        for i in range(1,a+1):
            s += (b**i)*i

        print(s)
    except EOFError:
        break