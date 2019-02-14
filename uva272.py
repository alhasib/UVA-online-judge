# c = 1
# while True:
#     try:
#         n = input()
#         for i in range(len(n)):
#             if n[i] == '"':
#                 if c%2 == 0:
#                     n.replace(n[i],"#")
#                 else:
#                     n.replace(n[i],"\``")
#             c += 1            
#         print(n)  
#     except EOFError:
#         break                          



c = 1
while True:
    try:
        n = input()
        n = list(n)
        for i in range(len(n)):
            # print(n[i])
            if n[i] == '"':
                if c%2 == 0:
                    n[i] = "''"
                    c += 1
                    # print(n)
                else:
                    n[i] = "``"
                    # print(n)
                    c += 1
        k = "".join(i for i in n)
        print(k) 
    except EOFError:
        break   