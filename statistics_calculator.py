print("Welcome to our Statistics Calculator")
listNumbers = [10, 900, 20, 30, 50, 60, 70, 10, 15, 23, 24, 54, 65, 78, 98, 100, 98, 189, 214, 450, 111, 2, 3, 4, 87]
# listNumbers = input("Enter a list of numbers separated by space \n").split()
max_num = listNumbers[0]
sortedList = []
highestFrequency = 0

def calculate_mean():
    sumNumbers = 0
    for number in listNumbers:
        sumNumbers += number
    print(f"The Mean of {listNumbers} is {sumNumbers/len(listNumbers)}")


calculate_mean()

# find the mode of the numbers
for i in range(0, len(listNumbers) - 1 ):
    if max_num < listNumbers[i]:
        max_num = listNumbers[i]

print(f"Max number is {max_num}")
