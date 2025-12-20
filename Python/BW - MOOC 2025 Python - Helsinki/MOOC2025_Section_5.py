### https://programming-25.mooc.fi/part-5
### Start Date:         12/16/2025
### Completion Date:    -
### Review / POW:
### - Sudoku Grid (Return: 01/01/2026)
### -
### -

def longest(strings: list):
    longest_val = 1
    longest_word = ""
        
    for word in strings:
        if len(word) > longest_val:
            longest_val = len(word)
            longest_word = word
    return longest_word

def sum_of_row(my_matrix, row_no: int):
    row = my_matrix[row_no]
    row_sum = 0
    for item in row:
        row_sum += item
    return row_sum

def sum_of_column(my_matrix, column_no:int):

    column_sum = 0
    for row in my_matrix:
        column_sum += row[column_no]
    return column_sum

def change_value(my_matrix, row_no: int, column_no: int, new_value: int):
    
    row = my_matrix[row_no] # find the row
    row[column_no] = new_value # find the row & the column location, then modify

def count_matching_elements(my_matrix: list, element:int):
    counter = 0
    for row in my_matrix:
        for val in row:
            if val == element:
                counter += 1
    return counter

def print_grid(sudoku):
    for row in sudoku:
        for square in row:
            if square > 0:
                print(f" {square}", end="")
            else: 
                print(" _", end="")

        print()

def who_won(game_board: list): 

    player1 = 0
    player2 = 0

    for row in game_board:
        for val in row:
            if val == 1:
                player1 += 1
            elif val == 2:
                player2 += 1
    if player1 > player2:
        return 1
    elif player2 > player1:
        return 2
    elif player1 == player2:
        return 0

def row_correct(sudoku: list, row_no: int):
    
    row = sudoku[row_no]
    unique = []
    for val in row:
        
        if val in unique and val != 0:
            return False
        else:
            unique.append(val)
    return True

def column_correct(sudoku: list, column_no: int):
    
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
#   (6, 0), (6, 3), (6, 6)

def double_items(numbers: list[int]) -> list[int]: 
    
    new_list = []
    for val in numbers:
        new_list.append(val*2)
    return new_list

 
def remove_smallest(numbers: list[int]):
        
    minVal = min(numbers)
    for val in numbers:
        if val == minVal:
            numbers.remove(val)   


def main():

    my_matrix = [[1, 21, 3], 
                 [3, 21, 1], 
                 [4, 5, 6]]

    print(my_matrix[0][0])
    print(my_matrix[1][2])

    m = [[1, 2, 1], 
         [0, 3, 4], 
         [1, 0, 0]]

    m_1 = [[1,24,3], 
          [3,200,1], 
          [4,5,6]]

    m_3 = [[4, 2, 3, 2], 
           [9, 1, 12, 11], 
           [7, 8, 9, 5], 
           [2, 9, 15, 1]]

    sudoku = [
          [9, 0, 0, 0, 8, 0, 3, 0, 0],
          [0, 0, 0, 2, 5, 0, 7, 0, 0],
          [0, 2, 0, 3, 0, 0, 0, 0, 4],
          [0, 9, 4, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 7, 3, 0, 5, 6, 0],
          [7, 0, 5, 0, 6, 0, 4, 0, 0],
          [0, 0, 7, 8, 0, 3, 9, 0, 0],
          [0, 0, 1, 0, 0, 0, 0, 0, 3],
          [3, 0, 0, 0, 0, 0, 0, 0, 2]]


    for row in m_1:
        print(f"Current Row: {row}")
        for val in row:
          print(val)
    print("End")

    for i in range(len(m_3)):
        for j in range(len(m_3[i])):
            m_3[i][j] += 10

    my_sum = sum_of_row(m_3, 0)
    my_column_sum = sum_of_column(m_3, 0)
    print(my_sum)
    print(my_column_sum)
    change_value(m_3, 0,0,12)
    print(m_3)
    print(count_matching_elements(m, 1))
    print_grid(sudoku)
    print(row_correct(sudoku, 2))
    print(column_correct(sudoku, 0))



if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers) 
    main()