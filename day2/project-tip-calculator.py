print("Welcome to the tip calculator!")
bill = input("What was the total bill ? $")
tip_percentage = input("What percentage tip would you like to give ? 10, 12, or 15 ? ")
people = input("How many people to split the bill ? ")

bill = float(bill)
percetage = int(tip_percentage)
people = int(people)

tip_total = bill * percetage / 100
pay_total = bill + tip_total

total_pay_per_person = round(pay_total/people, 2)

# formating for floating point : https://docs.python.org/3/tutorial/floatingpoint.html
total_pay_per_person = "{:.2f}".format(total_pay_per_person)

print(f"Each person should pay : ${total_pay_per_person}")