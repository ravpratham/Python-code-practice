# Replace every alternative char occurance with the charToChange
def replaceChar(content, charToReplace, charToChange, separator):
    phrases = content.split(separator)
    for phrase in phrases:
        rPosition = 0
        newPhrase = ""
        isFound = False
        for char in phrase:
            if (char.lower() == charToReplace):
                rPosition = rPosition + 1
                isFound = True
            else:
                isFound = False

            if (rPosition >= 2) and (isFound):
                rPosition = 0
                newPhrase = newPhrase + charToChange
            else:
                newPhrase = newPhrase + char
        print(newPhrase.strip())

#cont=input("enter a paragraph containing commas - \n")
cont = "Hello, My name is Pratham Rav, I have completed my 12th class"
replaceChar(cont, "a", "z", ",")
