def count(s):
    #counting with no OOP
    alphabetStrLower = ['a','b','c','d','e','f','g','h','i',
                          'j','k','l','m','n','o','p','q','r',
                             's','t','u','v','w','x','y','z']

    alphabetStrUpper = ['A','B','C','D','E','F','G','H','I',
                          'J','K','L','M','N','O','P','Q','R',
                             'S','T','U','V','W','X','Y','Z']
    counter = 0
    for letter in alphabetStrLower:
        if letter in s:
            counter = alphabetStrLower.count(letter)



print(count('aba'))
