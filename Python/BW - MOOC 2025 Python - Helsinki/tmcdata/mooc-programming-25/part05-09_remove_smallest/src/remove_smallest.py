def remove_smallest(numbers: list[int]):
        
    minVal = min(numbers)
    for val in numbers:
        if val == minVal:
            numbers.remove(val)