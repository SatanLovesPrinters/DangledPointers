def spruce(size):
    print("a spruce!")
    
    i = 0 

    while i < size:
        res = i % size
        if i % size == 0:
            print(i * "*")
            i += 1
        else:
            break

if __name__ == "__main__":
    spruce(5)