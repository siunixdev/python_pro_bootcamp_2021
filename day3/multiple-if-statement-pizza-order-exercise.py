# Dont chnage the code below
print("Welcome to pizza Deliveries!")
size = input("What size pizza do you want? S, M or L : ")
add_pepperoni = input("Do you want to peperoni ? Y or N : ")
extra_cheese = input("Do you wanto to extra cheese ? Y or N : ")
# Dont chnage the code above

# Small pizza = $15
# Medium Pizza = $20
# Large Pizza = $25

# pepperoni for small pizza = +$2
# pepperoni for medium or Large pizza = +$3

# extra cheese fot any size pizza = +$1

final_bill = 0

if size == "S" :
  final_bill += 15

elif size == "M" :
  final_bill += 20

else:
  final_bill += 25

if add_pepperoni == "Y" :
  if size == "S" :
    final_bill += 2
  else :
    final_bill += 3

if extra_cheese == "Y" :
  final_bill += 1

print(f"Your final bill is ${final_bill}")