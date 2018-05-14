case = 0
while True:
    case += 1
    n = int(input())
    if n == 0:
        break
    else:
        b = list(map(int,input().split()))
        s = sum(b)
        l = len(b)
        s = s/l
        move = 0
        for i in range(l):
            if b[i] > s:
                d = b[i] - s
                move += d

        print("Set #{}" .format(case))
        print("The minimum number of moves is {}." .format(int(move)))
        print()
