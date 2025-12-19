# https:/programming-25.mooc.fi/part-5
# WIP: Escaping on the column index is becoming a strange issue. 

def block_correct(sudoku: list[list[int]], row_no:int, column_no:int) -> bool :

    values = []
    for column in range(column_no, column_no + 3):
        for row in range(row_no, row_no + 3):
            value = sudoku[row][column]
            if value > 0:
                if value in values:
                    return False
                values.append(value)
        
    return True




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