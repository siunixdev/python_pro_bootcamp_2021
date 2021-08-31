#Step 1
import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
word_list_length = len(word_list)
random_word_list_index = random.randint(0, word_list_length-1)
random_word = (word_list[random_word_list_index])

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
letter_guess = input("Guess a letter : ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letter in random_word :
  if letter_guess == letter :
    print("Right")
  else :
    print("Wrong")