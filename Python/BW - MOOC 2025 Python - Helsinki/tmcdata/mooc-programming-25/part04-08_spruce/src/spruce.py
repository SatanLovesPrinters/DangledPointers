def spruce(size):
    print("a spruce!")
    
    i = 1
    treeLimit = size*2
    spacer = ''

    while (i % treeLimit) >= 0:
        spacerTotal = (treeLimit - i)
        spacerStringHalf = (spacerTotal//2)*' ' 
        posVal = i % treeLimit
        if posVal % 2 == 1:
            treeLimbs = (i * "*")
            print(spacerStringHalf + treeLimbs + spacerStringHalf)
            i += 1
        elif (i % treeLimit) == 0:
            i = 1
            spacerTotal = (treeLimit - i)
            spacerStringHalf = (spacerTotal//2)*' '
            print(spacerStringHalf + "*" + spacerStringHalf)
            break
        else:
            i+= 1

if __name__ == "__main__":
    spruce(5)