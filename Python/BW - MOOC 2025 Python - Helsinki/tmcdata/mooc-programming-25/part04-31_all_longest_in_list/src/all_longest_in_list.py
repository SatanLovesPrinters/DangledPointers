def all_the_longest(strList):
    longest = ""
    longestList = []
    maxFind = 0

    for word in strList:
        if len(word) >= len(longest):
            longest = word
            maxFind = len(longest)
            longestList.append(longest)
   
        for word in longestList:
            if len(word) < maxFind:
                longestList.remove(word)
                
    return longestList