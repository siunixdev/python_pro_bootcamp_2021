# Dont change the code below
print("Welcome to The Love Calculator")
name1 = input("What is your name ? \n")
name2 = input("What is their name ? \n")
# Dont change the code above

name = name1+name2
name_lower_case = name.lower()

# Get TRUE value
true_value = name_lower_case.count("t") + name_lower_case.count("r") + name_lower_case.count("u") + name_lower_case.count("e")

# Get LOVE value
love_value = name_lower_case.count("l") + name_lower_case.count("o") + name_lower_case.count("v") + name_lower_case.count("e")

true_love_value = int(str(true_value)+str(love_value))

if true_love_value < 10 or true_love_value > 90 :
  print(f"Your score is {true_love_value}, you go like coke and mentos")
elif true_love_value >= 40 and true_love_value <= 50 :
  print(f"Your score is {true_love_value}, you are alright together")
else :
  print(f"your score is {true_love_value}")