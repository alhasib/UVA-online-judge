n = int(input())
s = 0
for i in range(n):
    a,b = list(input().split())
    a.strip('0')
    b.strip('0')
    a = a[::-1]
    b = b[::-1]
    s = int(a) + int(b)
    s = str(s)
    s.strip('0')
    s = s[::-1]
    print(int(s))