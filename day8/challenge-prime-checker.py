#Write your code below this line ๐
def prime_checker(number) :
  devide_count = 0
  for i in range(1, number + 1):
    if number % i == 0:
      devide_count += 1

  if devide_count > 2 :
    print("It's not prime number")
  else :
    print("It's prime number")


#Write your code above this line ๐

#Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)