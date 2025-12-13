def greatest_number(a, b, c):
    if a >= b >= c or a >= c >= b:
        return a
    elif b >= a >= c or b >= c >= a:
        return b
    elif c >= a >= b or c >= b >= a:
        return c
        
if __name__ == "__main__":
    
    print(greatest_number(3, 4, 1))
    print(greatest_number(99, -4, 7))
    print(greatest_number(0, 0, 0))