from art import logo
print(logo)

def encrypt(encryption_type, my_text, shift):
    new_text = ''
    if shift > 26:
        shift = shift % 26
    if encryption_type == 'encode':
        for char in my_text:
            if char in alphabet:
                indexNumber = alphabet.index(char)
                newIndex = indexNumber + shift
                if newIndex >= 26:
                    newIndex -= 26
                new_text += alphabet[newIndex]
            else:
                new_text += char
        print(f"Encrypted letter of {my_text} is {new_text} \n")
    elif encryption_type == 'decode':
        for char in my_text:
            if char in alphabet:
                for letter in my_text:
                    indexNumber = alphabet.index(letter)
                    newIndex = indexNumber - shift
                    if newIndex < 0:
                        newIndex += 26
                    new_text += alphabet[newIndex]
            else:
                new_text += char
            print(f"Decrypted letter of {my_text} is {new_text} \n")
    else:
        print("You chose an incorrect number for the encryption")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = str(input("Type 'encode' to encrypt and 'decode' to decrypt: \n")).lower()
text = str(input("Enter a word to encode: \n")).lower()
continuation = str(input("Do you wish to continue this game: \n"))
shiftNumber = int(input("Enter a number to shift: \n"))
encrypt(encryption_type=direction, my_text=text, shift=shiftNumber)
