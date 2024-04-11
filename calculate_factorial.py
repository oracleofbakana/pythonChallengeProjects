print("Program to find the factorial of a number")
myNumber = int(input("Enter a number that is non-zero\n"))
factorialNumber = 1

if myNumber == 0:
    print("You entered 0 as a number. Enter a valid number")
else:
    range = myNumber
    while range > 1:
        factorialNumber *= range
        range -= 1
print(f"The factorial of {myNumber} is {factorialNumber}")
