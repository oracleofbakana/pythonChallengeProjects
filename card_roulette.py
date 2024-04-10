import random
print("Welcome to Our Restaurant\n")
names = input("Enter the first names of the diners separated by a comma\n")
namesSplit = names.split(",")
namesLength = len(namesSplit)
# print(namesLength)
randomNumber = random.randint(0, namesLength - 1)
print(f"{namesSplit[randomNumber]}  will pay our bills.")
