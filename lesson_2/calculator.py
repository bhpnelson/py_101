# Global language setting, modify this for different languages.
LANGUAGE = 'en'

import json
# Import json function to read json file

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def messages(message, lang='en'):
    return MESSAGES[lang][message]

# Function to format our prompts program-wide, including language.
def prompt(key):
    message = messages(key, LANGUAGE)
    print(f'=> {message}')

# Function that validates numbers
def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False


# PROGRAM BODY

# Say Hello.
while True:
    prompt('welcome')

    # Ask the user for the first number.
    prompt('number_prompt_1')
    number1 = input()

    # Validate user input.
    while invalid_number(number1):
        prompt('invalid_number')
        number1 = input()

    # Ask the user for the second number.
    prompt('number_prompt_2')
    number2 = input()

    # Validate user input.
    while invalid_number(number2):
        prompt('invalid_number')
        number1 = input()

    print(f'{number1} {number2}')

    # Ask the user for an operation to perform.
    prompt('operation_prompt')
    operation = input()

    # Validate user input
    while operation not in ["1", "2", "3", "4"]:
        prompt('invalid_operation')
        operation = input()

    # Perform the operation on the two numbers.
    match operation:
        case '1':   # '1' represents addition
            output = float(number1) + float(number2)
        case '2':   # '2' represents subtraction
            output = float(number1) - float(number2)
        case '3':   # '3' represents multiplication
            output = float(number1) * float(number2)
        case '4':   # '4' represents division
            output = float(number1) / float(number2)


    # Print the result to the terminal.
    print(f'The result is {output}')

    prompt('another_operation')
    answer = input()
    if answer and answer[0].lower() != 'y':
        break





