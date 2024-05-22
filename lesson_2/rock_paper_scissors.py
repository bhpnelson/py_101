import random

# Constants

VALID_CHOICES = {'r': 'rock',
                 'p' : 'paper',
                 'sc' : 'scissors',
                 'l' : 'lizard',
                 'sp' : 'spock',
                 'ro': 'rock',
                 'pa' : 'paper',
                 'sci' : 'scissors',
                 'li' : 'lizard',
                 'spo' : 'spock',
                 'roc' : 'rock',
                 'pap' : 'paper',
                 'scis' : 'scissors',
                 'liz' : 'lizard',
                 'spoc' : 'spock',
                 'pape' : 'paper',
                 'sciss' : 'scissors',
                 'liza' : 'lizard',
                 'scisso' : 'scissors',
                 'lizar' : 'lizard',
                 'scissor' : 'scissors',
}

ALL_VALID_INPUTS = (
    list(VALID_CHOICES.values()) + list(VALID_CHOICES.keys())
)

WIN_CONDITIONS = {
                'rock' : ['scissors', 'lizard'],
                'paper' : ['rock', 'spock'],
                'scissors' : ['paper', 'lizard'],
                'spock' : ['scissors', 'rock'],
                'lizard' : ['spock', 'paper']
}

# Define functions.

def prompt(message):
    print(f"==> {message}")

def format_choice(unformatted_input):
    if unformatted_input in list(VALID_CHOICES.values()):
        return unformatted_input
    elif unformatted_input in VALID_CHOICES:
        return VALID_CHOICES[unformatted_input]
    else:
        prompt("That's not a valid choice")
        return None

def display_winner():
    prompt(f"You chose {player_choice}, computer chose {computer_choice}")
    if computer_choice in WIN_CONDITIONS[player_choice]:
        prompt("You win!")
        return 'Player'
    elif player_choice in WIN_CONDITIONS[computer_choice]:
        prompt("Computer wins!")
        return 'Computer'
    else:
        prompt("It's a tie!")

def score_counter(round_winner):
    if round_winner == 'Player':
        current_score['Player'] += 1
    elif round_winner == 'Computer':
        current_score['Computer'] += 1
        
def score_display():
    print(f'+--------------SCORE----------------+')
    print(f'|   {current_score}    |')
    print(f'+-----------------------------------+')

def end_game():
    if current_score['Player'] >= 3:
        game_winner = 'Player'
        return game_winner
    
    if current_score['Computer'] >=3:
        game_winner = 'Computer'
        return game_winner
    
    return None

current_score = {'Player' : 0, 'Computer' : 0}

# Main Program Loop.
prompt("Welcome to SPOCK PAPER LIZARD !!!")
prompt("Best of 3 wins is the champion.")
prompt(f"""It's easy to remember:
        Rock beats {' and '.join(WIN_CONDITIONS['rock'])}
        Paper beats {' and '.join(WIN_CONDITIONS['paper'])}
        Scissors beats {' and '.join(WIN_CONDITIONS['scissors'])}
        Spock beats {' and '.join(WIN_CONDITIONS['spock'])}
        Lizard beats {' and '.join(WIN_CONDITIONS['lizard'])}
""")

while True:
    prompt(f'''Choose one: {', '.join(WIN_CONDITIONS)}.
You may use an abbreviation.''')
    unformatted_input = input().lower().strip()
# Validate user input.
    while unformatted_input not in ALL_VALID_INPUTS:
        prompt("That's not a valid choice. Re-enter:")
        unformatted_input = input().lower().strip()

    player_choice = format_choice(unformatted_input)

    computer_choice = random.choice(list(WIN_CONDITIONS.keys()))

    score_counter(display_winner())

    score_display()

    # Ends game if someone gets to 3 points.
    if end_game() is not None:
        prompt(f'''The winner is {end_game()}!
               GAME OVER.''')

    # Reset the score if game ends and player selects to play again.
        current_score = {'Player' : 0, 'Computer' : 0}
        prompt("Do you want to play again (y/n)?")
        answer = input().lower()
        while answer == '' or (answer[0] != 'n' and answer[0] != 'y'):
            prompt('Please enter "y" or "n".')
            answer = input().lower()

        if answer[0] != "y":
            break