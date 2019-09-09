import copy
matrix_no = 0
main_q = []

print("Enter The Goal Matrix: ")
goal_matrics = []
for row in range(3):          
    coloumn =[] 
    for col in range(3):      
        coloumn.append(int(input())) 
    goal_matrics.append(coloumn)

print("this is goal {}" .format(goal_matrics))

print("Enter the initial state") 
matrix = [] 
        
for i in range(3):          
    a =[] 
    for j in range(3):      
        a.append(int(input())) 
    matrix.append(a) 

matrix_no += 1
matrix.append(matrix_no)
matrix_parent_number = 0 
matrix.append(matrix_parent_number)    
main_q.append(matrix)


parent_q = []

for i in main_q:
    parent_q.append(i)
    parent = i[-2]
    i = i[:-2]
    copy_matrix = copy.deepcopy(i)
    if i == goal_matrics:
        matched_matrix = copy.deepcopy(i)
        break
    else:
        r = 0
        c = 0
        for itm in i:
            if 0 in itm:
                col = itm.index(0)
                new_matrix = copy.deepcopy(copy_matrix)
                 
                if r == 2 and col == 1:
                    #upmove
                    replaced_value = new_matrix[r-1][col]
                    new_matrix[r-1][col] = 0
                    new_matrix[r][col] = replaced_value
                    matrix_no += 1
                    new_matrix.append(matrix_no)
                    new_matrix.append(parent)
                    main_q.append(new_matrix)
                    
                    # right move
                    new_matrix = copy.deepcopy(copy_matrix)

                    replaced_value = new_matrix[r][col + 1]
                    new_matrix[r][col + 1] = 0
                    new_matrix[r][col] = replaced_value

                    matrix_no += 1
                    new_matrix.append(matrix_no)
                    new_matrix.append(parent)

                    main_q.append(new_matrix)

                    # print(main_q)

                    #left move
                    new_matrix = copy.deepcopy(copy_matrix)

                    replaced_value = new_matrix[r][col - 1]
                    new_matrix[r][col - 1] = 0
                    new_matrix[r][col] = replaced_value

                    matrix_no += 1
                    new_matrix.append(matrix_no)
                    new_matrix.append(parent)

                    main_q.append(new_matrix)

                elif r == 2 and col == 2:
                    #Up move

                    new_matrix = copy.deepcopy(copy_matrix)

                    replaced_value = new_matrix[r-1][col]
                    new_matrix[r-1][col] = 0
                    new_matrix[r][col] = replaced_value

                    matrix_no += 1
                    new_matrix.append(matrix_no)
                    new_matrix.append(parent)
                    main_q.append(new_matrix)
                        
                    #left move

                    new_matrix = copy.deepcopy(copy_matrix)

                    replaced_value = new_matrix[r][col-1]
                    new_matrix[r][col-1] = 0
                    new_matrix[r][col] = replaced_value

                    matrix_no += 1
                    new_matrix.append(matrix_no)
                    new_matrix.append(parent)

                    main_q.append(new_matrix)

                elif r == 2 and col == 0:

                    #up move

                    new_matrix = copy.deepcopy(copy_matrix)

                    replaced_value = new_matrix[r-1][col]
                    new_matrix[r-1][col] = 0
                    new_matrix[r][col] = replaced_value

                    matrix_no += 1
                    new_matrix.append(matrix_no)
                    new_matrix.append(parent)

                    main_q.append(new_matrix)

                    # right move

                    new_matrix = copy.deepcopy(copy_matrix)

                    replaced_value = new_matrix[r][col + 1]
                    new_matrix[r][col+1] = 0
                    new_matrix[r][col] = replaced_value

                    matrix_no += 1
                    new_matrix.append(matrix_no)
                    new_matrix.append(parent)

                    main_q.append(new_matrix)

                elif r == 1 and col == 0:    

                    #up move

                    new_matrix = copy.deepcopy(copy_matrix)

                    replaced_value = new_matrix[r-1][col]
                    new_matrix[r-1][col] = 0
                    new_matrix[r][col] = replaced_value

                    matrix_no += 1
                    new_matrix.append(matrix_no)
                    new_matrix.append(parent)

                    main_q.append(new_matrix) 

                    #down move

                    new_matrix = copy.deepcopy(copy_matrix)

                    replaced_value = new_matrix[r+1][col]
                    new_matrix[r+1][col] = 0
                    new_matrix[r][col] = replaced_value

                    matrix_no += 1
                    new_matrix.append(matrix_no)
                    new_matrix.append(parent)

                    main_q.append(new_matrix)

                    #right move

                    new_matrix = copy.deepcopy(copy_matrix)

                    replaced_value = new_matrix[r][col + 1]
                    new_matrix[r][col+1] = 0
                    new_matrix[r][col] = replaced_value

                    matrix_no += 1
                    new_matrix.append(matrix_no)
                    new_matrix.append(parent)

                    main_q.append(new_matrix)

                elif r == 1 and col == 1:
                    #up move
                    new_matrix = copy.deepcopy(copy_matrix)

                    replaced_value = new_matrix[r-1][col]
                    new_matrix[r-1][col] = 0
                    new_matrix[r][col] = replaced_value

                    matrix_no += 1
                    new_matrix.append(matrix_no)
                    new_matrix.append(parent)

                    main_q.append(new_matrix)

                    #down move
                    new_matrix = copy.deepcopy(copy_matrix)

                    replaced_value = new_matrix[r+1][col]
                    new_matrix[r+1][col] = 0
                    new_matrix[r][col] = replaced_value

                    matrix_no += 1
                    new_matrix.append(matrix_no)
                    new_matrix.append(parent)

                    main_q.append(new_matrix)

                    #left move
                    new_matrix = copy.deepcopy(copy_matrix)

                    replaced_value = new_matrix[r][col - 1]
                    new_matrix[r][col-1] = 0
                    new_matrix[r][col] = replaced_value

                    matrix_no += 1
                    new_matrix.append(matrix_no)
                    new_matrix.append(parent)

                    main_q.append(new_matrix)

                    #right move

                    new_matrix = copy.deepcopy(copy_matrix)

                    replaced_value = new_matrix[r][col + 1]
                    new_matrix[r][col+1] = 0
                    new_matrix[r][col] = replaced_value

                    matrix_no += 1
                    new_matrix.append(matrix_no)
                    new_matrix.append(parent)

                    main_q.append(new_matrix)

                elif r == 1 and col == 2:
                    #up move
                    new_matrix = copy.deepcopy(copy_matrix)

                    replaced_value = new_matrix[r-1][col]
                    new_matrix[r-1][col] = 0
                    new_matrix[r][col] = replaced_value

                    matrix_no += 1
                    new_matrix.append(matrix_no)
                    new_matrix.append(parent)

                    main_q.append(new_matrix)

                    #down move

                    new_matrix = copy.deepcopy(copy_matrix)

                    replaced_value = new_matrix[r+1][col]
                    new_matrix[r+1][col] = 0
                    new_matrix[r][col] = replaced_value

                    matrix_no += 1
                    new_matrix.append(matrix_no)
                    new_matrix.append(parent)

                    main_q.append(new_matrix)

                    #lef move

                    new_matrix = copy.deepcopy(copy_matrix)

                    replaced_value = new_matrix[r][col - 1]
                    new_matrix[r][col-1] = 0
                    new_matrix[r][col] = replaced_value

                    matrix_no += 1
                    new_matrix.append(matrix_no)
                    new_matrix.append(parent)

                    main_q.append(new_matrix)

                elif r == 0 and col == 0:

                    # down move

                    new_matrix = copy.deepcopy(copy_matrix)

                    replaced_value = new_matrix[r+1][col]
                    new_matrix[r+1][col] = 0
                    new_matrix[r][col] = replaced_value

                    matrix_no += 1
                    new_matrix.append(matrix_no)
                    new_matrix.append(parent)

                    main_q.append(new_matrix)

                    #right move

                    new_matrix = copy.deepcopy(copy_matrix)

                    replaced_value = new_matrix[r][col + 1]
                    new_matrix[r][col+1] = 0
                    new_matrix[r][col] = replaced_value

                    matrix_no += 1
                    new_matrix.append(matrix_no)
                    new_matrix.append(parent)

                    main_q.append(new_matrix) 

                elif r == 0 and col == 1:

                    #down move

                    new_matrix = copy.deepcopy(copy_matrix)

                    replaced_value = new_matrix[r+1][col]
                    new_matrix[r+1][col] = 0
                    new_matrix[r][col] = replaced_value

                    matrix_no += 1
                    new_matrix.append(matrix_no)
                    new_matrix.append(parent)

                    main_q.append(new_matrix)

                    # left move

                    new_matrix = copy.deepcopy(copy_matrix)

                    replaced_value = new_matrix[r][col - 1]
                    new_matrix[r][col-1] = 0
                    new_matrix[r][col] = replaced_value

                    matrix_no += 1
                    new_matrix.append(matrix_no)
                    new_matrix.append(parent)

                    main_q.append(new_matrix)

                    # right move    

                    new_matrix = copy.deepcopy(copy_matrix)

                    replaced_value = new_matrix[r][col + 1]
                    new_matrix[r][col+1] = 0
                    new_matrix[r][col] = replaced_value

                    matrix_no += 1
                    new_matrix.append(matrix_no)
                    new_matrix.append(parent)

                    main_q.append(new_matrix)

                elif r == 0 and col == 2:

                    #down move

                    new_matrix = copy.deepcopy(copy_matrix)

                    replaced_value = new_matrix[r+1][col]
                    new_matrix[r+1][col] = 0
                    new_matrix[r][col] = replaced_value

                    matrix_no += 1
                    new_matrix.append(matrix_no)
                    new_matrix.append(parent)

                    main_q.append(new_matrix)

                    # left move

                    new_matrix = copy.deepcopy(copy_matrix)

                    replaced_value = new_matrix[r][col - 1]
                    new_matrix[r][col-1] = 0
                    new_matrix[r][col] = replaced_value

                    matrix_no += 1
                    new_matrix.append(matrix_no)
                    new_matrix.append(parent)

                    main_q.append(new_matrix)
                        

            else:
                 r += 1

print("Matrix Number Is: {}" .format(parent_q[-1][-2]))
print("Parent Number Is: {}" .format(parent_q[-1][-1]))

for j in range(3):
    for k in range(3):
        print(parent_q[-1][j][k], end = " ")
    print('')
print('')    

parent_n = parent_q[-1][-1]



while len(parent_q) > 0:  
    if parent_n == 0:
        break
    else:

        for i in parent_q:
            # print(i)
                h = copy.deepcopy(i)
                if i[-2] == parent_n:
                    parent_n = i[-1]
                    matrix_number = i[-2]
                    parent_number = i[-1]
                    print("Matrix Number Is: {}" .format(matrix_number))
                    print("Parent Number Is: {}" .format(parent_number))
                    print("Matrix Is: ")
                    i = i[:-2]
                    for j in range(3):
                        for k in range(3):
                            print(i[j][k], end = " ")
                        print('')
                    print('')
                    # if h[-1] == 0:
                    #     break 
                    parent_q.remove(h) 
                   

