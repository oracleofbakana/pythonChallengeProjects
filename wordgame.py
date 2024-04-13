import random
words = ['William','Nancy', 'Blogger', 'Love', 'Dapper']
print(words)
# chosen_word = str(input("Guess a word from the list above\n"))
chosen_word = random.choice(words)
print(chosen_word)
new_words = []
chosen_letter = str(input("Now Guess a letter from the word for the word games to begin\n")).lower()
for letter in chosen_word:
    i = 0
    if letter ==  chosen_letter:
        new_words.append(letter)
        print(f"{new_words[i]}")
    else:
        new_words.append("_")
#        print(f"{chosen_word[i]}")
print(new_words)