while True:
    try:
        n,k = list(map(int,input().split()))
        count = n
        while(n>=k):
            count += int(n/k)
            n = int(n/k) + int(n%k)
        print(count)
    except EOFError:
        break