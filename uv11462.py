while True:
    try:
        n = int(input())
        if n == 0:
            break
        else:
            age = list(map(int, input().split()))
            age.sort()
            k = " ".join(str(s) for s in age)
            # for j in age:
            print(k)    
    except EOFError:
        break            



        