t = int(input())
for g in range(t):
    n = input()
    l = []
    f = n.replace(" ", '')
    for i in f:
        l.append(int(i))
    ln = len(f)
    for j in range(0,ln,2):
        k = l[j]
        l[j] = str(int(k) * 2)
        d = str(l[j])
        s = 0
        for m in d:
            s += int(m)
        l[j] = s 

    if sum(l) % 10 == 0:
        print("Valid")
    else:
        print("Invalid")          
            