# BMI Caculator Exercise
# Body mass index

# Dont change the code below
height = input("Enter your height in m : ")
weight = input("Enter your weight in kg : ")
# Dont change the code above

bmi = float(weight) / float(height) ** 2

print("Your BMI is " + str(int(bmi)))