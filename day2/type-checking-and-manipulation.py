# Type error, Type Checking and Type Conversion
num_char = len(input("What is your name ? "))
# print("Your name has " + num_char + " characters.") # it will be show error type

print(type(num_char))
# because the data type is integer we must conver the data type to string to print it with string
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

# for example
a = float(123)
print(type(a))

# so what happen if i do this
print(100 + float("33.21"))

# what about this line
print(str(70) + str(100))