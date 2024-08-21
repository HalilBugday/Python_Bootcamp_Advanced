print("Welcome to the Tip Calculator!")
bill = float(input("What is the total bill? (type is $)\n"))
tip = int(input("Waht percentage tip would you like to give? (10-15-20)\n"))
people = int(input("How many people to split the bill?\n"))

tip_as_percent = tip / 100
total_tip_amount = bill + tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people

final_amount = round(bill_per_person, 2) #2 digit
print(f"Each person should pay: ${final_amount}")
