# https:/programming-25.mooc.fi/part-5

def sum_of_row(my_matrix, row_no: int):
    row = my_matrix[row_no]
    row_sum = 0
    for item in row:
        row_sum += item
    return row_sum


def sum_of_column(my_matrix, column_no: int):
    column_sum = 0
    for row in my_matrix:
        column_sum += row[column_no]
    return column_sum


m = [[4, 2, 3, 2], [9, 1, 12, 11], [7, 8, 9, 5], [2, 9, 15, 1]]
my_sum = sum_of_row(m, 1)
my_sum_2 = sum_of_column(m, 2)
print(my_sum)
print(my_sum_2)