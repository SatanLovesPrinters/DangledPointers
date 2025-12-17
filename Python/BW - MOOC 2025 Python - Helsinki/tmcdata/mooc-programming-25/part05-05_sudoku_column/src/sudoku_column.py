def column_correct(sudoku: list, column_no: int):
    
    unique = []
    for rowVal in sudoku:
        if rowVal[column_no] in unique and rowVal[column_no] != 0:
            return False
        else:
            unique.append(rowVal[column_no])
    return True