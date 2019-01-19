def checker(a):
    ss = int(a) + int(a[::-1])
    return ss

t = int(input())
for i in range(t):
    n = int(input())
    s = str(n)
    c = 0
    while s != s[::-1]:
        c += 1
        d = checker(s)
        if str(d) == str(d)[::-1]:
            print(str(c) + " " + str(d) )
            # print(d)
            break
        else:
            s = str(d)
            continue 
            
