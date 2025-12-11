def line(val, string):
    
    if len(string) >= 1:
        string = string[0]
    elif len(string) == 0:
        string = "*"
    res = val * string
    print(res)

def square_of_hashes(size):
     
    #square = length * width
    i = 0
    while i < size:
        line(size, "#")
        i += 1


if __name__ == "__main__":
    square_of_hashes(3)
