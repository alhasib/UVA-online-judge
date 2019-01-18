import math
n = int(input())
for i in range(n):
    a,b = input().split()
    if int(a) >= int(b):
        aa = int(a)/2
        bb = int(b)/2
        ab = aa + bb
        ad = aa - bb
        if math.floor(ab) == ab and math.floor(ad) == ad:

            print(str(int(ab)) + " " + str(int(ad)))
        else:
            print("impossible")    
    else:
        print("impossible")