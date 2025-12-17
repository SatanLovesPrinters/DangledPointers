def count_matching_elements(my_matrix: list, element:int):
    counter = 0
    for row in my_matrix:
        for val in row:
            if val == element:
                counter += 1
    return counter