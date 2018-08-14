# # l = list(map(int,input().split()))
# # for i in l:
# #     c = l.count(i)
# #     print("{} {}" .format(i,c))
# #     while i in l:
# #         l.remove(i)
#
#
# l = list(map(int,input().split()))
# ul = []
# print(l)
# i = l[0]
# for i in l:
#     #print(i)
#     if i not in ul:
#         ul.append(i)
#         c = l.count(i)
#         print("{} {}".format(i, c))

import sys
numbers = [int(x) for x in sys.stdin.read().split()]
used_list = []
for num in numbers:
    if num not in used_list:
        used_list.append(num)
        c = numbers.count(num)
        print("{} {}".format(num, c))

