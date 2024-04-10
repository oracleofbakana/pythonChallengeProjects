print(f"Program to Sum  all Even numbers from start to end")
startNumber = int(input("Enter a starting number \n"))
endNumber = int(input("Enter a ending number \n"))
totalEven = 0
if startNumber > endNumber:
    print("Starting number can not be greater than Ending Number")
    exit(0)
elif startNumber == endNumber:
    print("Starting number can not be equal to ending number")
    exit(0)
else:
    for number in range(startNumber, endNumber):
        if number % 2 == 0:
            totalEven += number
#            print(f"This is an even Number: {number}")

#        else:
#            print(f"This is an odd Number: {number}")
print(f"Total even numbers between {startNumber} and {endNumber} is {totalEven}")