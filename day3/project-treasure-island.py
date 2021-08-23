print("Welcoma to Treasure Island")
print("Your mission is to find the treasure")
print("======================================")
left_right = input("You're at a cross road. Where do you wanto to go ? type 'left' or 'right'\n")
if left_right.lower() == 'right' :
  print("You fell into a hole. Game Over")
else :
  swim_wait = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait  for a boat. Type 'swim' to swim across.\n")
  if swim_wait.lower() == 'swim' :
    print("You got attecked by an angry trout. Game Over")
  else :
    door_color = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
    if door_color.lower() == "red" :
      print("It's room full of fire. Game Over")
    elif door_color.lower() == "blue" :
      print("You enter a room of beasts. Game Over")
    else :
      print("You found the treasure! You Win!")