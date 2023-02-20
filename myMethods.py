import random
characters = list("abcçdefgğhuıijklmnoöpqrsştuüvwxyz0123456789\"!'^+%&/()=?_; ,*-|`}][{½$#£<>âß@")
__bigLetters = list("abcçdefgğhuıijklmnoöpqrsştuüvwxyz".upper())

for i in __bigLetters:
    characters.append(i)

def find(x, list):
    indexes = []
    for i in range(len(list)):
        if x in list:
            if list[i] == x:
                indexes.append(str(i))
        else:
            indexes.append("not found")
            break

    return indexes

def hideToText(yourText):
    hidden = ""

    listYourText = list(yourText)

    while(listYourText != []):
        for i in range(random.randint(0, 10)):             #
            hidden = hidden + random.choice(characters)    #

        hidden = hidden + ""
        
        a = len(yourText) #getting the length of YourText
        b = random.randint(1, a) #getting a random number that not longer than your text
        c = listYourText[0 : b] #getting characters of random length from the first letters of your text

        hidden = hidden + "".join(c)

        for i in c:                 #removing the characters that we get with c variable
            listYourText.remove(i)  #

        hidden = hidden + "é"

    for i in range(random.randint(0, 10)):
        hidden = hidden + random.choice(characters)

    return hidden

        
def findFromText(text):
    found = ""

    a = find("æ", text)
    b = find("é", text)

    for i in range(len(text)):
        found = found + text[int(a[i] + 1) : int(b[i])]
    
    return found