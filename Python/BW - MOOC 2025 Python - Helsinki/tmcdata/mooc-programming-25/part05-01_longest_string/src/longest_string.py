def longest(strings: list):
    longest_val = 1
    longest_word = ""
        
    for word in strings:
        if len(word) > longest_val:
            longest_val = len(word)
            longest_word = word
    return longest_word


if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))