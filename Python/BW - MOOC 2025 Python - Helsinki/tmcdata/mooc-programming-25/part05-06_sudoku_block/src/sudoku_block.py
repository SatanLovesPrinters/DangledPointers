def block_correct(sudoku:list, row_no:int, column_no:int):

    row_check = False
    column_check = False

    row_limit = sudoku[row_no+2]
    block_limit = sudoku[row_no+2][column_no+2]
    
    unique = []
    for rowVal in row_limit:
        if rowVal in unique and rowVal != 0:
            return False
        else:
            unique.append(rowVal)
        row_check = True
    
    unique = []
    for rowVal in range(block_limit):
        for columnVal in row_limit:
            if columnVal in unique and columnVal != 0:
                return False
            else:
                unique.append(columnVal)

    column_check = True

    if row_check == True and column_check == True:
        return True
    else:
        return False