import math
while True:
    try:
        n = int(input())
        if n == 0:
            break
        else:
            a = math.floor(math.sqrt(n))
            b = math.ceil(math.sqrt(n))
            if a == b:
                print("yes")
            else:
                print("no")

    except EOFError:
        break

