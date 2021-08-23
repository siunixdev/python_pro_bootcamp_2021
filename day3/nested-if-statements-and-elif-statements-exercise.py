# BMI Caculator 2.0
# Body mass index

# Dont change the code below
height = input("Enter your height in m : ")
weight = input("Enter your weight in kg : ")
# Dont change the code above

bmi = float(weight) / float(height) ** 2

bmi_interpretation = ""

if bmi < 18.5 :
  bmi_interpretation = "Underwight"
elif bmi < 25 :
  bmi_interpretation = "Normal weight"
elif bmi < 30 :
  bmi_interpretation = "Overweight"
elif bmi < 35 :
  bmi_interpretation = "Obese"
else :
  bmi_interpretation = "Clinically obese"

print(f"Your BMI is {bmi} you are {bmi_interpretation}")