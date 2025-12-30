def friend(x):
    #check for names that are 4 characters in length
    results = []
    i = 0
    while i < len(x):
        if len(x[i]) == 4:
            results.append(x[i])
            i+=1
        else:
            i+=1
    return results

print(friend(["Jeff", "Squid", "Soccer", "Chec"]))