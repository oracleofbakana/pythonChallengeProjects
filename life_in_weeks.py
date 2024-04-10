print("Program to solve Life In weeks challenge")

presentAge = int(input("What is your present age?\n"))

remainingAge = 90 - presentAge

remainingWeeks = remainingAge * 52
remainingDays = remainingAge * 365
remainingMonths = remainingAge * 12

#output using f string

message = f"You have {remainingAge} years, {remainingMonths} months, {remainingWeeks} weeks and {remainingDays} days"
print(message)
