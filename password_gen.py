import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
specialCharacters = ['#', '$', '&', '^', '(', ')', '*', '!', '%', '+']

print("Program to generate a random password")
nr_letters = int(input("How many letters do you want your password to contain?\n"))
nr_symbols = int(input("How many special characters do you want your password to contain?\n"))
nr_numbers = int(input("How many numbers do you want your password to contain?\n"))

randomPassword = []
password = ""

for i in range(0, nr_letters):
    randomPassword.append(random.choice(letters))

for i in range(0, nr_symbols):
    randomPassword.append(random.choice(specialCharacters))

for i in range(0, nr_numbers):
    randomPassword.append(str(random.choice(numbers)))

print(f"RandomPassword using the Easy Level is {randomPassword}\n")

random.shuffle(randomPassword)
print(f"Password List shuffled is {randomPassword}")

for char in randomPassword:
    password += char

print(f"Password list is {password}")