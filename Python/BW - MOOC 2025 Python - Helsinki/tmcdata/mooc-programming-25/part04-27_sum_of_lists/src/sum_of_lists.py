def list_sum(listIntA, listIntB):
    resultsList = []
    i = 0 
    while i < len(listIntA):
        results = listIntA[i] + listIntB[i]
        resultsList.append(results)
        i += 1
    return resultsList