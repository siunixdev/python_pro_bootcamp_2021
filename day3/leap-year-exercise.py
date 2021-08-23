# Dont change the code below
year = int(input("Which year do you want to check ? "))
# Dont change the code above

leap_status = ""

if year % 4 == 0 :
  if year % 100 == 0 :
    if year % 400 == 0 :
      leap_status = "Leap"
    else :
      leap_status = "Not Leap"
  else :
    leap_status = "Leap"
else :
  leap_status = "Not leap"

print(f"{leap_status} year.")