n = int(input())
l = []
for i in range(n):
    a = {}
    nn = int(input())
    for j in range(nn):
        sub, d  = input().split()
        a[sub] = d
    dt = int(input())
    s = input()
    if s in a.keys():
        dd = a[s]
        if int(dd) <= dt:
            l.append("Yesss")
        elif int(dd) <= (dt + 5):
            l.append("Late")
        else:
            l.append("Do your own homework!")
    else:
        l.append("Do your own homework!")                 
t = 1
for g in l:
    print("Case {}: {}" .format(t,g))
    t += 1
