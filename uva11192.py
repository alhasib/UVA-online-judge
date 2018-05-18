while True:
    n = list(input().split())
    c = int(n[0])
    if int(n[0]) == 0:
        break
    else:
        ns = n[1]
        cc = int(len(ns) / c)
        lp = []
        ns = n[1]
        while (len(ns)>0):
            bb = ns[:cc]
            bb =  bb[::-1]
            ns = ns[cc:]
            lp.append(bb)

        kk = "".join(lp)
        print(kk)



# for i in range(1,101):
#     a,s = input().split()
#     l = []
#     ls = len(s)
#     v = int(ls/int(a))
#     while (len(s) > 0):
#         bb = s[:v]
#         bb =  bb[::-1]
#         s = s[v:]
#         l.append(bb)
#     k = "".join(l)
#     print(k)