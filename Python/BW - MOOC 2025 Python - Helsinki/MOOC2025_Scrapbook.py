# https://programming-25.mooc.fi/part-4

def range_of_list(my_list : list):
    greatest = max(my_list)
    smallest = min(my_list)
    rangeVal = greatest - smallest
    return rangeVal

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    result = range_of_list(my_list)
    print("The range of the list is", result)