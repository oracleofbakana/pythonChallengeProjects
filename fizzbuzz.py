print("Program to simulate the Fizz Buzz game\n")

for number in range(1,101):
    if number == 0:
        print("0 is not a number")
        number += 1
    elif number % 3 == 0 and number % 5 == 0:
        print( "FizzBuzz")
    elif number % 5 ==0:
        print("Buzz")
    elif number % 3 == 0 :
        print("Fizz")
    else:
        print(number)
