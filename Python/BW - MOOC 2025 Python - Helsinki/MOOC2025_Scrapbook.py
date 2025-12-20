# https:/programming-25.mooc.fi/part-5
#   Box Out: 
#   (0, 0), (0, 3), (0, 6), | [0][0], [0][2], [0][5],
#   (3, 0), (3, 3), (3, 6), | [2][0], [2][2], [2][5],
#   (6, 0), (6, 3), (6, 6)  | [5][0], [5][2], [5][5]

def print_sudoku(sudoku: list[int]):

    newList = []


    for column in sudoku:
        print()
        for val in column:
    
            if val == 0: print(" ", end="")

            else:
                print(val)


     

def add_number(sudoku: list[int], row_no: int, column_no: int, number_input:int):
    
    sudoku[row_no][column_no] = number_input
    


sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

print_sudoku(sudoku)
add_number(sudoku, 0, 0, 2)
add_number(sudoku, 1, 2, 7)
add_number(sudoku, 5, 7, 3)
print()
print("Three numbers added:")
print()
print_sudoku(sudoku)