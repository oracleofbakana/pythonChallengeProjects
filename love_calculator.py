print("Welcome to Love Calculator")

name1 = input("What is the first person's name?\n")
name2 = input("What is the lover's name?\n")

name = f"{name1} {name2}".lower()
countLetterT = int(name.count("t"))
countLetterR = int(name.count("r"))
countLetterU = int(name.count("u"))
countLetterE = int(name.count("e"))

countLetterL = int(name.count("l"))
countLetterO = int(name.count("o"))
countLetterV = int(name.count("v"))
countLetterE2 = int(name.count("e"))

countMessage = f" T occurs {countLetterT} times\n R occurs {countLetterR} times\n U occurs {countLetterU} times\n E occurs {countLetterE} times\n L occurs {countLetterL} times\n O occurs {countLetterO} times\n V occurs {countLetterV} times\n E occurs {countLetterE2} times\n"

countTRUE = str(countLetterT + countLetterR + countLetterU + countLetterE)
countLOVE = str(countLetterL + countLetterO + countLetterV + countLetterE)

loveScore = countTRUE+countLOVE
loveScore_toInt = int(loveScore)
print(countMessage)

if (loveScore_toInt < 10) or (loveScore_toInt > 90):
    print(f"Your Love Score is {loveScore}, you go together like coke and mentos")
elif (loveScore_toInt >= 40) and (loveScore_toInt <= 50):
    print(f"Your Love Score is {loveScore}, you are alright together")
else:
    print(f"Your Love Score is {loveScore}.")

