import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

your_choose = int(input("What do you choose ? type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choose = random.randint(0, 2)

game_image = [rock, paper, scissors]

if your_choose < 0 or your_choose > 2 :
  print("Invalid input, You Lose!")
else :
  print(game_image[your_choose])

  print("Computer chose : ")
  print(game_image[computer_choose])

  if your_choose == computer_choose:
    print("Draw")
  else :
    if your_choose == 0 and computer_choose == 2 or your_choose == 2 and computer_choose == 1 or your_choose == 1 and computer_choose == 0:
      print("You Win!")
    else :
      print("You Lose!")
