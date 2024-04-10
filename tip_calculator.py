print("Welcome to Tip Calculator")
bill = float(input("Enter your bill in dollars?\n$"))
percentTip = int(input("How much TIP would you like to pay? 10%, 15% 0r 20%?\n"))
billPayers = int(input("How many people would share the bill\n"))

totalBill = bill + (percentTip/100 * bill)
individualPayment = round(totalBill/billPayers)
totalBill = "{:.2f}".format(totalBill)
individualPayment = "{:.2f}".format(individualPayment)
message = f"Total Bill is ${totalBill} and each person would pay ${individualPayment}"
print(message)
