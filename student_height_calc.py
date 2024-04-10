print("Program to calculate student's height\n")

# studentsHeight = [180, 214, 165, 173, 189, 169, 146]
# 180 214 165 173 189 169 146
studentsHeight = input("Enter a list of student heights separated by comma\n").split()
# print(studentsHeight)
for n in range(0, len(studentsHeight)):
    studentsHeight[n] = int(studentsHeight[n])
#    print(f" {studentsHeight[n]}\n")

totalHeight = studentsCount = 0

for height in studentsHeight:
    totalHeight += height
    studentsCount += 1

averageHeight = totalHeight/studentsCount
print(f"Total Height of the {studentsCount} students is {totalHeight}\n")
print(f"Average Height of the {studentsCount} students is {averageHeight}\n")
