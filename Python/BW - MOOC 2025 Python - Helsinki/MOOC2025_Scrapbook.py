# https:/programming-25.mooc.fi/part-5
# WIP: Escaping on the column index is becoming a strange issue. 

def block_correct(sudoku:list, row_no:int, column_no:int):
    
    block_start = sudoku[row_no][column_no]
    block_limit = sudoku[row_no+2][column_no+2]

    row_limit = sudoku[row_no+2]
    #figure out iterating over 3x3 blocks/4x4/5x5 blocks 
    #- if we can check every 'grid' amount of blocks then we can modify based on other conditions.    
    

    row_check = False
    column_check = False

    

def block_correct_v0(sudoku:list, row_no:int, column_no:int):
    
    row_start = sudoku[row_no]
    row_limit = sudoku[row_no+2]

    column_start = sudoku[row_no][column_no]
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


print(block_correct(sudoku, 0, 0)) #limit would be [2][2]
print(block_correct(sudoku, 1, 2)) #limit would be [3][4]
print(block_correct(sudoku, 0, 6))