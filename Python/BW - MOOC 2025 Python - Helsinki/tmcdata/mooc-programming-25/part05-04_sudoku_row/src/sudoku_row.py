def row_correct(sudoku: list, row_no: int):
    
    row = sudoku[row_no]
    unique = []
    for val in row:
        
        if val in unique and val != 0:
            return False
        else:
            unique.append(val)
    return True