import random

VALID_CHOICES = {'r': 'rock', 
                 'p' : 'paper', 
                 'sc' : 'scissors', 
                 'l' : 'lizard', 
                 'sp' : 'spock'
}

SEARCHABLE_VALID_CHOICES = list(VALID_CHOICES.values()) + list(VALID_CHOICES.keys())

WIN_CONDITIONS = {
                'rock' : ['scissors', 'lizard'],
                'paper' : ['rock', 'spock'],
                'scissors' : ['paper', 'lizard'],
                'spock' : ['scissors', 'rock'],
                'lizard' : ['spock', 'paper']
}

current_score = {'Player' : 0, 'Computer' : 0}

def prompt(message):
    print(f"==> {message}")

def format_choice(unformatted_input):
    if unformatted_input in list(VALID_CHOICES.values()):
        return unformatted_input
    elif unformatted_input in list(VALID_CHOICES.keys()):
        return VALID_CHOICES[unformatted_input]
    else:
        prompt("That's not a valid choice")
        return None

def display_winner(player, computer):
    prompt(f"You chose {player_choice}, computer chose {computer_choice}")

    if computer_choice in WIN_CONDITIONS[player_choice]:
        round_winner = 'Player'
        prompt("You win!")
        score_counter_and_display(round_winner)
    elif player_choice in WIN_CONDITIONS[computer_choice]:
        round_winner = 'Computer'
        prompt("Computer wins!")
        score_counter_and_display(round_winner)
    else:
        prompt("It's a tie!")

def score_counter_and_display(round_winner):
    if round_winner == 'Player':
        current_score['Player'] += 1
        prompt(f'The current score is {current_score}')
    elif round_winner == 'Computer':
        current_score['Computer'] += 1
        prompt(f'The current score is {current_score}')

def end_game():
    if current_score['Player'] >= 3:
        game_winner = 'Player'
        return game_winner
    elif current_score['Computer'] >=3:
        game_winner = 'Computer'
        return game_winner
    else:
        return None

# Main Program Loop.

while True:
    prompt(f"Welcome to SPOCK PAPER LIZARD !!!")
    prompt(f'''Choose one: {list(VALID_CHOICES.values())}.
You may use the first letter or first two letters (for S) as an abbreviation.''')
    unformatted_input = input().lower().strip()
    # Validate user input.
    while unformatted_input not in SEARCHABLE_VALID_CHOICES:
        prompt("That's not a valid choice. Re-enter:")
        unformatted_input = input().lower().strip()
    
    player_choice = format_choice(unformatted_input)

    computer_choice = random.choice(list(VALID_CHOICES.values()))

    display_winner(player_choice, computer_choice)

    # Ends game if someone gets to 3 points.
    if end_game() != None:
        prompt(f"The winner is {end_game()}!")

    # Reset the score if game ends and player selects to play again.
        current_score = {'Player' : 0, 'Computer' : 0}
        prompt("Do you want to play again (y/n)?")
        answer = input().lower()
        while answer == '' or (answer[0] != 'n' and answer[0] != 'y'):
            prompt('Please enter "y" or "n".')
            answer = input().lower()

        if answer[0] != "y":
            break

