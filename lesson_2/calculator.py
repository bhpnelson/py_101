import json
# Import json function to read json file

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)
    
# Function to format our prompts program-wide
def prompt(message):
    print(f"==> {message}")

# Function that validates numbers
def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True
    return False


# PROGRAM BODY

# Say Hello.
while True:
    prompt('Welcome to Calculator')

    # Ask the user for the first number.
    prompt("What's the first number?")
    number1 = input()

    # Validate user input.
    while invalid_number(number1):
        prompt("Hmm... that doesn't look like a valid number.")
        number1 = input()

    # Ask the user for the second number.
    prompt("What's the second number?")
    number2 = input()

    # Validate user input.
    while invalid_number(number2):
        prompt("Hmm... that doesn't look like a valid number.")
        number1 = input()

    print(f'{number1} {number2}')

    # Ask the user for an operation to perform.
    prompt("""
        'What operation would you like to perform?\n1) Add 2) Subtract 3) Multiply 4) Divide')
        """)
    operation = input()

    # Validate user input
    while operation not in ["1", "2", "3", "4"]:
        prompt("You must choose 1, 2, 3, or 4")
        operation = input()

    # Perform the operation on the two numbers.
    match operation:
        case '1':   # '1' represents addition
            output = int(number1) + int(number2)
        case '2':   # '2' represents subtraction
            output = int(number1) - int(number2)
        case '3':   # '3' represents multiplication
            output = int(number1) * int(number2)
        case '4':   # '4' represents division
            output = int(number1) / int(number2)


    # Print the result to the terminal.
    print(f"The result is: {output}")

    prompt('Would you like to perform another operation? (y/n) ')
    answer = input()
    if answer and answer[0].lower() != 'y':
        break





