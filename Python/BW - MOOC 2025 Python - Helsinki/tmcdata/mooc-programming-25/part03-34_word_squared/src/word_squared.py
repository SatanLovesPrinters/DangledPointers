def squared(text, val):
    boxField = ""
    boxLimit = val**2         
    
    for i in range(boxLimit):  
        boxField +="\n"*(i%val==0)*(i!=0) 
        boxField += text[i%len(text)]

    print(boxField)