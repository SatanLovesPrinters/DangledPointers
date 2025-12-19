# https:/programming-25.mooc.fi/part-5
# Please write a function named sudoku_grid_correct(sudoku: list)

#  - takes a two-dimensional array sudoku grid as its argument. 
#  - function should use functions from the 3 previous exercises to determine whether the complete sudoku grid is filled in correctly. 
#  - Copy the functions from the exercises above into your Python code file for this exercise.

#   Checks:
#  - 9x Rows, 
#  - 9x Columns
#  - 3x3x3 blocks in the grid. 

#  - If all contain each of the numbers 1 to 9 at most once, return True. 
#  - If a single one is filled in incorrectly, return False.

#   Boxes to check: 
#   (0, 0), (0, 3), (0, 6), 
#   (3, 0), (3, 3), (3, 6), 
#   (6, 0), (6, 3), (6, 6).

def row_correct(sudoku: list[list[int]], row_no: int):
    
    row = sudoku[row_no]
    unique = []
    for val in row:
        
        if val in unique and val != 0:
            return False
        else:
            unique.append(val)
    return True

def column_correct(sudoku: list[list[int]], column_no: int):
    
    unique = []
    for rowVal in sudoku:
        if rowVal[column_no] in unique and rowVal[column_no] != 0:
            return False
        else:
            unique.append(rowVal[column_no])
    return True

def block_correct(sudoku: list[list[int]], row_no:int, column_no:int) -> bool:

    values = []
    for column in range(column_no, column_no + 3):
        for row in range(row_no, row_no + 3):
            value = sudoku[row][column]
            if value > 0: 
                if value in values:
                    return False
                values.append(value)
        
    return True



#Test Cases

sudoku1 = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]


sudoku2 = [
  [2, 6, 7, 8, 3, 9, 5, 0, 4],
  [9, 0, 3, 5, 1, 0, 6, 0, 0],
  [0, 5, 1, 6, 0, 0, 8, 3, 9],
  [5, 1, 9, 0, 4, 6, 3, 2, 8],
  [8, 0, 2, 1, 0, 5, 7, 0, 6],
  [6, 7, 4, 3, 2, 0, 0, 0, 5],
  [0, 0, 0, 4, 5, 7, 2, 6, 3],
  [3, 2, 0, 0, 8, 0, 0, 5, 7],
  [7, 4, 5, 0, 0, 3, 9, 0, 1]
]

print(sudoku_grid_correct(sudoku1)) #False

print(sudoku_grid_correct(sudoku2)) #True