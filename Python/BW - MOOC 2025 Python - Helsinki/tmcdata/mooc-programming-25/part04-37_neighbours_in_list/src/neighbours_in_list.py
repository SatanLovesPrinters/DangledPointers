def longest_series_of_neighbours(my_list):
    num_neighbors_count = 0
    num_neighbors_max = 0
    
    for num1, num2 in zip(my_list, my_list[1:]):
        if num1+1==num2 or num1-1==num2:
            num_neighbors_count += 1
            if num_neighbors_count >= num_neighbors_max:
                    num_neighbors_max = num_neighbors_count
        else:
            if num_neighbors_count >= num_neighbors_max:
                    num_neighbors_max = num_neighbors_count
            num_neighbors_count = 0
            
    return num_neighbors_max+1