# Dont change the code below
age = input("What is your current age ? ")
# Dont change the code above

# There are 365 days in year, 52 weeks in year and 12 months in year


age = int(age)
different_year = 90 - age

days = different_year * 365
weeks = different_year * 52
months = different_year * 12

text = f"You have {days} days, {weeks} weeks and {months} months left."
print(text)