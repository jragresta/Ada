#Rock, Paper, Scissors v3
print ("Welcome to Rock, Paper, Scissors!\n\n\n\n")
import random

def choose_rps():
    "output: randomly returns rock, paper, or scissors"
    r = random.randint(0,2)
    if r == 0:
        return "rock"
    elif r == 1:
        return "scissors"
    else:
        return "paper"
      
player1 = choose_rps()

player2 = choose_rps()

def rps (player1, player2):
  print(f"Player 1 chose {player1}\n\nPlayer 2 chose {player2}\n")

  # print(f"Player 2 chose {player2}")

  """
  input: player1 and player2 -> 'rock','paper', 'scissors'
  output: "Player 1 wins!", "Player 2 Wins!", "It's a tie!"
  """
  #check if tie
  if player1 == player2:
      print('It\'s a tie!\n\n')
  # player1 is rock
  elif player1 == 'rock':
      if player2 == 'scissors': 
        print('Player 1 won!\n\n')
      elif player2 == 'paper':
        print('Player 2 won!\n\n')
  # player1 is paper
  elif player1 == 'paper':
      if player2 == 'rock': 
        print('Player 1 won!\n\n')
      elif player2 == 'scissors':
        print('Player 2 won!\n\n')
  # player1 is scissors
  elif player1 == 'scissors':
      if player2 == 'paper': 
        print('Player 1 won!')
      elif player2 == 'rock':
        print('Player 2 won!\n\n')

import random
def play_again():
    r = random.randint(0, 1)

    return r == 0

play = True
while play:
  rps (player1, player2)  
  play = play_again()
print("Thank you for playing!\n\n")

