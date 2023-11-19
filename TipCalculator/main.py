print("Welcome to the tip calculator")

total_bill = float(input("What was the total bill?"))
percentage = float(input("What percentage tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))

total_payment = total_bill + total_bill * percentage / 100
per_person = total_payment / people
formatted = "{:.2f}".format(per_person)

print(f"Each person should pay {formatted}$")
