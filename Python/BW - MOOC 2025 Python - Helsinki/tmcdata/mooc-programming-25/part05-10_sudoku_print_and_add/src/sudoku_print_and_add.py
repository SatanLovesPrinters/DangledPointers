def print_sudoku(sudoku: list[int]):
    for column in sudoku:
        for val in column:
            if val == 0:
                print(" _", end=" ")
            else:
                print(val, end=" ")
        print()

def add_number(sudoku: list[int], row_no: int, column_no: int, number_input:int):
    
    sudoku[row_no][column_no] = number_input
    
