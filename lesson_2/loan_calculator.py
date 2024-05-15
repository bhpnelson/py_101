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
    prompt('Welcome to Mortgage & Loan Calculator')

    # Ask the user for the loan amount.
    prompt("What's the loan amount? Do not use dollar sign.")
    loan_amount = float(input())

    # Validate user input.
    while invalid_number(loan_amount):
        prompt("Hmm... that doesn't look like a valid number.")
        loan_amount = float(input())

    # Ask the user for the APR (Annual Percentage Rate).
    prompt("What's the APR in percentage form?")
    yearly_rate = float(input()) / 100

    # Validate user input.
    while invalid_number(yearly_rate):
        prompt("Hmm... that doesn't look like a valid number.")
        yearly_rate = float(input()) / 100

    # Ask the user for the loan duration in years.
    prompt("What's the loan duration in years?")
    year_duration = float(input())

    # Validate user input.
    while invalid_number(year_duration):
        prompt("Hmm... that doesn't look like a valid number.")
        year_duration = float(input())

    # Check inputs (debugging).
    print(f'{loan_amount} {yearly_rate} {year_duration}')

    # Calculate monthly interest rate.
    monthly_rate = float(yearly_rate) / 12

    # Calculate loan duration in months.
    month_duration = float(year_duration) * 12

    # Check conversions to monthly.
    print(f'Monthly Rate: {monthly_rate} Duration in Months: {month_duration}')

    # Calculate monthly payment.
    monthly_payment = loan_amount * (
        monthly_rate /
            (1 - (1 + monthly_rate) ** (-month_duration))
    )

    # Calculate payment rounded to two decimal places.
    output = round(monthly_payment, 2)

    # Print the result to the terminal.
    print(f"The result is: ${output}")

    prompt('Would you like to perform another operation? (y/n) ')
    answer = input()
    if answer and answer[0].lower() != 'y':
        break