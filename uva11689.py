n = int(input())
for i in range(n):
    a,b,c = list(map(int,input().split()))
    count = 0
    d = a+b
    while(d>=c):
        count += int(d/c)
        d = int(d/c) + int(d%c)
    print(count)