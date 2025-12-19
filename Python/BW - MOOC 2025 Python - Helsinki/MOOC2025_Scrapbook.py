# https:/programming-25.mooc.fi/part-5
# WIP: Escaping on the column index is becoming a strange issue. 

def block_correct_v02(sudoku:list, row_no:int, column_no:int):

    row_check = False
    column_check = False

    row_limit = sudoku[row_no+2]
    block_limit = sudoku[row_no+2][column_no+2]
    
    unique = []
    for rowVal in row_limit:
        if rowVal in unique and rowVal != 0:
            row_check = False
            break
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


sudoku = [
  [ 9, 0, 0, 0, 8, 0, 3, 0, 0 ],   # row 0
  [ 2, 0, 0, 2, 5, 0, 7, 0, 0 ],   # row 1
  [ 0, 2, 0, 3, 0, 0, 0, 0, 4 ],   # row 2
  [ 2, 9, 4, 0, 0, 0, 4, 0, 0 ],   # row 3
  [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],   # row 4
  [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],   # row 5
  [ 0, 0, 7, 8, 0, 3, 9, 0, 0 ],   # row 6
  [ 0, 0, 1, 0, 0, 0, 0, 0, 3 ],   # row 7
  [ 3, 0, 1, 0, 0, 8, 0, 0, 2 ],   # row 8
]


print(block_correct(sudoku, 0, 0)) # False 
print(block_correct(sudoku, 0, 3)) # True (Currently: False)
print(block_correct(sudoku, 0, 6)) # True (Currently: False)