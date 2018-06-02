while True:
    try:
        a = int(input())
        b = int(input())
        print(int(a*b))
    except EOFError:
        break