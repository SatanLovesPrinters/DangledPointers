def block_correct(sudoku:list, row_no:int, column_no:int):
    
    row_limit = sudoku[row_no+2]
    column_limit = sudoku[row_no+2][column_no+2]

    row_check = False
    column_check = False

    unique = []
    for val in range(len(row_limit)):
        if val in unique and val != 0:
            return False
        else:
            unique.append(val)
    row_check = True 
    
    unique = []
    for row in sudoku:

        if row[column_no] in unique and row[column_no] != 0:
            return False
        else:
            unique.append(row[column_no])
    return True
    
    if column_check == True and row_check == True:
        return True
    else:
        return False