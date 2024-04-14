def encrypt(myText, shift):
    newText = ''
    for letter in myText:
        indexNumber = alphabet.index(letter)
        newIndex = indexNumber + shift
        if newIndex >= 25:
            newIndex -= 26
        newText += alphabet[newIndex]
#        print(f"{indexNumber} \n")
#        print(f"The {indexNumber} which is {indexNumber}  - - has an {encodedNumber}so the new string is --{newText}")
    print(f"{newText} \n")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt and 'decode' to decrypt: \n")
text = str(input("Enter a word to encode: \n"))
shiftNumber = int(input("Enter a number to shift: \n"))
encrypt(myText=text, shift=shiftNumber)
