print("Welcome to the Treasure Map game\n")
row1 = ["🎁", "🎁", "🎁"]
row2 = ["🎁", "🎁", "🎁"]
row3 = ["🎁", "🎁", "🎁"]
print(f" {row1}\n {row2}\n {row3}")
rowMap = [row1, row2, row3]

position = input("Where do you want to put the treasure?\n")

horizontal = int(position[0])
vertical = int(position[1])

selectedRow = rowMap[vertical - 1]
selectedRow[horizontal - 1] = "X"

print(f" {row1}\n {row2}\n {row3}")
