print("Program to calculate Students score")

studentScore = input("Enter the students score (without space)\n").split()

for n in range(0, len(studentScore)):
    studentScore[n] = int(studentScore[n])
#   print(studentScore[n])
#   print(f"\n {type(studentScore[n])}")

maxScore = studentScore[0]
for score in studentScore:
    if score > maxScore:
        maxScore = score
print(f"Maximum score of the numbers is {maxScore}")