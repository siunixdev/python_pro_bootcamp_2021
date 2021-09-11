from art import logo

print(logo)

final_bid = []

def add_bid(name, bid):
  new_item = {
    "name" : name,
    "bid" : bid,
  }

  final_bid.append(new_item)

def get_winner():
  current_bid = 0
  current_name = ""
  for item in final_bid:
    max = int(item['bid'])
    name = item['name']
    if max > current_bid :
      current_bid = max
      current_name = name

  winner = {
    "name" : current_name,
    "bid" : current_bid
  }

  return winner

print("Welcome to the secret auction program.")
repeat = True
while repeat :
  name = input("What is your name ? ")
  bid = input("What is your bid ? ")

  add_bid(name, bid)

  repeat_question = input("Are there any other bidders ? Type 'yes' or 'no'\n")
  if repeat_question == 'no':
    winner = get_winner()
    print(f"The winner is {winner['name']} with a bid of ${winner['bid']}")
    repeat = False