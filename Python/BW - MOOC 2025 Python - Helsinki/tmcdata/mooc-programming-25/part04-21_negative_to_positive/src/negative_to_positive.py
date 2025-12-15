valinput = int(input("Please type in a positive integer: "))

for i in range(-(valinput),valinput+1):
    if i == 0:
        i += 1
    else:
        print(i)
        i += 1