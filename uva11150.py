while True:
    try:

        n = int(input())
        count = n
        n += 1
        while(n):
            if n < 3:
                break
            else:
                v = int(n/3)
                count += v
                vs = n%3
                n = v + vs
        print(count)
    except EOFError:
        break


# while True:
#     n = int(input())
#     count = n
#     while(n>=3):
#         v = int(n/3)
#         count += v
#         vs = n%3
#         n = v + vs
#         if n == 2:
#             count += 1
#     print(count)