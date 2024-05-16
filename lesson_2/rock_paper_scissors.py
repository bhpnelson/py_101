import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']

def prompt(message):
    print(f"==> {message}")

def display_winner(player, computer):
    prompt(f"You chose {choice}, computer chose {computer_choice}")

    if ((choice == "rock" and computer_choice == "scissors") or
        (choice == "rock" and computer_choice == "lizard") or
        (choice == "paper" and computer_choice == "rock") or
        (choice == "paper" and computer_choice == "spock") or
        (choice == "scissors" and computer_choice == "paper") or
        (choice == "scissors" and computer_choice == "lizard") or
        (choice == "spock" and computer_choice == "scissors") or
        (choice == "spock" and computer_choice == "rock") or
        (choice == "lizard" and computer_choice == "spock") or
        (choice == "lizard" and computer_choice == "paper")
    ):
        prompt("You win!")
    elif ((choice == "rock" and computer_choice == "paper") or
        (choice == "rock" and computer_choice == "spock") or
        (choice == "paper" and computer_choice == "scissors") or
        (choice == "paper" and computer_choice == "lizard") or
        (choice == "scissors" and computer_choice == "rock") or
        (choice == "scissors" and computer_choice == "spock") or
        (choice == "spock" and computer_choice == "paper") or
        (choice == "spock" and computer_choice == "lizard") or
        (choice == "lizard" and computer_choice == "rock") or
        (choice == "lizard" and computer_choice == "scissors")
    ):
        prompt("Computer wins!")
    else:
        prompt("It's a tie!")

while True:
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input()

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    display_winner(choice, computer_choice)

    prompt("Do you want to play again (y/n)?")
    answer = input().lower()
    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break

        prompt('Please enter "y" or "n".')
        answer = input().lower()

    if answer[0] == 'n':
        break


