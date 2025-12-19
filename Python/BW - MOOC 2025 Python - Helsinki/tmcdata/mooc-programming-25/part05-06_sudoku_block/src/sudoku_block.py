def block_correct(sudoku: list[list[int]], row_no:int, column_no:int):

    values = []
    for column in range(column_no, column_no + 3):
        for row in range(row_no, row_no + 3):
            value = sudoku[row][column]
            if value > 0:
                if value in values:
                    return False
                values.append(value)
        
    return True
