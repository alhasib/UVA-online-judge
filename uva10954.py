while True:
    n = int(input())
    if n == 0:
        break
    else:

        l = list(map(int,input().split()))
        l.sort()
        p = []
        while len(l) > 1:
            l.sort()
            a = l[0] 
            b = l[1]
            s = a + b
            p.append(s)
            l.remove(a)
            l.remove(b)
            l.insert(0,s)
        
        print(sum(p))    

