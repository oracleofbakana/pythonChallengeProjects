words = ['William','Nancy', 'Blogger', 'Love', 'Dapper']
print(words)
chosen_word = str(input("Guess a word from the list above\n"))

chosen_letter = str(input("Now Guess a letter from the word for the word games to begin\n")).lower()
for letter in chosen_word:
    i = 0
    if letter ==  chosen_word[i]:
        print("There is a letter in the word")
    else:
        print("No letter in the word")
