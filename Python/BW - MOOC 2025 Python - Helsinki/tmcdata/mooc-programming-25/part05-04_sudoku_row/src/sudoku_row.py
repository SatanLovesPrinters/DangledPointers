def row_correct(sudoku: list, row_no: int):
    
    row = sudoku[row_no]
    unique = []
    for element in row:
        
        if element in unique and element != 0:
            return False
        else:
            unique.append(element)
    return True