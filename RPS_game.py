import random

def get_choices():
  options = ["rock","paper","scissors"]
  player_choice = input("enter a choice:")
  computer_choice = random.choice(options)
  choices = {"player":player_choice,"computer":computer_choice}

  return choices

def check_win(player, computer):
  print(f"you chose {player},computer chose {computer}")
  if player == computer:
    return "Its a tie"
  elif player == "rock":
    if computer == "scissors":
      return "PLayer won"
    else:
      return "Computer won"
  elif player == "paper":
    if computer == "rock":
      return "player won"
    else:
      return "Computer won"
  elif player == "scissors":
    if computer == "rock":
      return "player lost"
    else:
      return "Player won"

choices = get_choices()
result = check_win(choices["player"],choices["computer"])
print(result)
