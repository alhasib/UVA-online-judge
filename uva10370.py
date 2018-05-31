n = int(input())
while n>0:
    marks = list(map(int,input().split()))
    mark = marks[1:]
    mn = marks[0]
    avrage = sum(marks[1:])/mn
    count = 0
    for i in mark:
        if i > avrage:
            count += 1
    final_result = (count/mn)*100
    print("{0:0.3f}%" .format(final_result))
    n -= 1