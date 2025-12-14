def first_word(text):
    
    sentenceList = text.split()
    return sentenceList[0]

def second_word(text):

    sentenceList = text.split()
    return sentenceList[1]
   
def last_word(text):
 
    sentenceList = text.split()
    return sentenceList[-1]

if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))