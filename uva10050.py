T = int(input()) #test case
for i in range(T):
    N = int(input()) #days
    p = int(input()) #number of partys
    jl = [] #list for all friday and saturday
    for j in range(0,N,7):
        s = j + 7
        f = s - 1
        jl.append(f)
        jl.append(s)
        j = s
    # print(jl)

    pl = []
    for k in range(p):
        pin = int(input()) #hartal parameter
        for m in range(0,N,pin):
            n = m + pin
            if n not in jl and n <= N:
                pl.append(n)
    f_list = list(set(pl)) #remove duplicate value from the list using set()
    print(len(f_list))