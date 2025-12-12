### https://programming-25.mooc.fi/part-4
### Start Date:         12/10/2025
### Completion Date:    -
### Review / POW:
### - Iterating on a specific condition | Escaping on a specific index (Resolved with Discord review on Modulo %)
### - 
### - 


# Quick intro on string conversion
# Utilize dir() for help in the python console

def SimpleSomethingModulo(high, low):
    a = high
    b = low
    
    while b <= a:
        message = f"A mod B: {a} % {b} = {a % b} || B mod A: {b} % {a} = {b % a}"    
        print(message)
        b += 1
        lineSep = len(message) * "-"
    
    print(lineSep)
 

def spruce(size):
    print("a spruce!")
    
    i = 1
    treeLimit = size*2

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
    SimpleSomethingModulo(10, 1)
    SimpleSomethingModulo(6, 1)