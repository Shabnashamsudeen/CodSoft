import random

def play_round():
  
  user_choice = input("Choose rock, paper, or scissors : ").lower()
  computer_choice = random.choice(['rock', 'paper', 'scissors'])
  
  # Determine winner 
  win_lookup = {
    'rock': {'scissors': True, 'paper': False},
    'paper': {'rock': True, 'scissors': False},
    'scissors': {'paper': True, 'rock': False},
  }

  winner = None
  if user_choice == computer_choice:
    winner = 'tie'
  else:
    winner = 'user' if win_lookup[user_choice][computer_choice] else 'computer'

  return user_choice, computer_choice, winner

def main():
 
  print("Welcome to Rock-Paper-Scissors!")
  play_again = 'y'

  while play_again.lower() == 'y':
    user_choice, computer_choice, winner = play_round()

    # Display choices and result
    print(f"You chose {user_choice}, computer chose {computer_choice}.")
    if winner == 'tie':
      print("It's a tie!")
    else:
      print(f"{winner.capitalize()} wins!")

    play_again = input("Play again? (y/n): ")

  print("Thanks for playing!")

if __name__ == "__main__":
  main()
  