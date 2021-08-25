#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

total_of_letter = len(letters)
total_of_number = len(numbers)
total_of_symbol = len(symbols)

# Easy
password_letter = ""
password_number = ""
password_symbol = ""

for letter in range (0, nr_letters):
  random_letter = letters[random.randint(0, total_of_letter-1)]
  password_letter += random_letter

for number in range (0, nr_numbers):
  random_number = numbers[random.randint(0, total_of_number-1)]
  password_number += random_number

for symbol in range (0, nr_symbols):
  random_symbol = symbols[random.randint(0, total_of_symbol-1)]
  password_symbol += random_symbol

password = password_letter+password_symbol+password_number

print(f"Your easy password is {password}")


# Hard
password_list = list(password)
random.shuffle(password_list)

hard_password = ""
for char in password_list:
  hard_password += char

print(f"Your hard password is {hard_password}")