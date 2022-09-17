# Importing random to get a choice
import random
# Start the game function
def play():
    user = input("Write 'r' for rock, 'p' for paper, or 's' for scissors: ").lower()
    computer = random.choice(['r','p','s'])

    # In case of invalid input
    if (user != 'r') and (user != 'p') and (user != 's'):
        return "Invaild input. Try again"

    # In case of a tie
    if user == computer:
        return f"The computer choose {computer}. It's a tie!"
    if is_win(user, computer):
        return f'The computer choose {computer}.You Won.'
    return f'The computer choose {computer}.You lost.'

# In case of a user win
def is_win(player, opponent):   
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True
    
print(play())