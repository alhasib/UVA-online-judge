while True:
    l = []
    n = int(input())
    if n == 0:
        break
    else:

        for i in range(n):
            s = input()
            # l = len(n)
            c = s.count(" ")
            l.append(c)

        l.sort()
        ll = len(l)

        count_sum = 0
        for j in range(ll):
            if l[j] > l[0]:
                d = l[j] - l[0]
                count_sum += d

        print(count_sum)