def prime_number(number):
    is_prime = True
    for i in range(2, number - 1):
        if number % i == 0:
           is_prime = False
    if is_prime:
        print(f"{number} is not a prime number")
    else:
        print(f"{number} is a prime number")



my_number = int(input("Enter a number to check if it is a prime number: \n"))
prime_number(number=my_number)

