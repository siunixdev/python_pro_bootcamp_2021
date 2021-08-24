import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# Don't change the code above

# Write your code below this line
peoples = len(names)
peoples_number = random.randint(0, peoples-1)

name = names[peoples_number]

print(f"{name} is going to buy the meal today!")