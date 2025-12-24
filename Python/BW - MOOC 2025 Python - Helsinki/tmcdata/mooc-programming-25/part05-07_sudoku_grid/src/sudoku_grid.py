def row_correct(sudoku: list, row_no: int):
    
    row = sudoku[row_no]
    elements = []
    for element in row:
        if element in elements and element != 0:
            return False
        else:
            elements.append(element)
    return True

def column_correct(sudoku: list, column_no: int):
    
    elements = []
    for rowVal in sudoku:
        if rowVal[column_no] in elements and rowVal[column_no] != 0:
            return False
        else:
            elements.append(rowVal[column_no])
    return True

def block_correct(sudoku: list[list[int]], row_no:int, column_no:int):

    elements = []
    for column in range(column_no, column_no + 3):
        for row in range(row_no, row_no + 3):
            value = sudoku[row][column]
            if value > 0:
                if value in elements:
                    return False
                elements.append(value)
        
    return True

def sudoku_grid_correct(sudoku: list):
    i = 0
    truths = []
    while i < 9:
        if row_correct(sudoku, i) == True and column_correct(sudoku, i) == True and block_correct(sudoku, i, i) == True:
            truths.append(True)
            i+=1
        if row_correct(sudoku, i) == False or column_correct(sudoku, i) == False or block_correct(sudoku, i, i) == False:
            truths.append(False)
            i+=1
        
    if False in truths:
        return False
    elif False not in truths:
        return True


sudoku = [
  [ 6, 4, 9, 2, 8, 3, 1, 5, 7 ],
  [ 0, 5, 0, 6, 4, 9, 2, 3, 8 ],
  [ 2, 3, 8, 1, 5, 7, 6, 4, 9 ],
  [ 9, 2, 3, 8, 1, 5, 0, 6, 4 ],
  [ 7, 6, 4, 9, 2, 3, 8, 1, 5 ],
  [ 8, 1, 5, 7, 0, 4, 9, 2, 0 ],
  [ 5, 7, 6, 4, 9, 2, 3, 2, 1 ],
  [ 4, 0, 2, 3, 8, 1, 5, 0, 6 ],
  [ 3, 0, 1, 5, 0, 6, 4, 9, 0 ],
]
print(sudoku_grid_correct(sudoku))

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

print(sudoku_grid_correct(sudoku1))

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

print(sudoku_grid_correct(sudoku2))