counter = 0
words = []

while True:
    word = input("Word: ")
    if word not in words:
        words.append(word)
        counter += 1
    elif word in words:
        print(f"You typed in {counter} different words")
        break