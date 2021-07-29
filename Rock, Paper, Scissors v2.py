#Rock, Paper, Scissors v2
def rps (player1, player2):
  """
  input: player1 and player2 -> 'rock','paper', 'scissors'
  output: "Player 1 wins!", "Player 2 Wins!", "It's a tie!"
  """
  #check if tie
  if player1 == player2:
      print('It\'s a tie!')
  # player1 is rock
  elif player1 == 'rock':
      if player2 == 'scissors': 
        print('Player 1 won!')
      elif player2 == 'paper':
        print('Player 2 won!')
  # player1 is paper
  elif player1 == 'paper':
      if player2 == 'rock': 
        print('Player 1 won!')
      elif player2 == 'scissors':
        print('Player 2 won!')
  # player1 is scissors
  elif player1 == 'scissors':
      if player2 == 'paper': 
        print('Player 1 won!')
      elif player2 == 'rock':
        print('Player 2 won!')

rps('rock', 'paper')