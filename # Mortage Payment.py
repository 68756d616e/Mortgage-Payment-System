# Mortage Payment

# Basic version 
# Mortage calculator
# Welcome message
print("Welcome to a mortage payment system")

while True:

    print() # Empty space
    # Home price & what is a home price
    home_price = int(input("Please enter the amount of the mortgage £"))

    # Down payment & what is a down payment
    down_payment = input("Please choose a % or £")
    percentage_amount = 0
    type = "%"
    type2 = "GBP £"
    down_payment_percentage_amount = 0
    down_payment_pound_amount = 0

    if down_payment == 'Percentage %':
        down_payment_percentage_amount = float(input("Please enter the amount of the percentage as a decimal. Example 0.2 :"))
        loan_amount = home_price - down_payment_percentage_amount
        
    elif down_payment == "£":
        down_payment_pound_amount = float(input("Please enter the amount the pound :"))
        loan_amount = home_price = down_payment_pound_amount
    else:
        print("Please type % or £")
        
    # Loan term & what is a loan term
    loan_term = int(input("How long will the loan term be? :"))

    # Interest rate & what is a interest rate
    interest_rate = float(input("What is the interst rate, example %6.5 : "))

    # Start date month and year - Either indivual inputs or one singular input
    start_date_month = input("Please type the month. Example jan or january : ")
    start_date_year = int(input("Please type year. Example 2022 : "))
    month_year = (start_date_month, start_date_year)

    # Calculation
    # Down payment result - Home price minus the amount of the down payment, the down payment is calculated with either a % or £
    loan_amount_result = down_payment_pound_amount - home_price

    # Loan Term calculation
    loan_duration = 12 * loan_term  # The amount of mortgage payments

    # Result
    if down_payment == "%":
        print(f"""Please find the Mortgage results below!
    Home Price : £{home_price}
    Loan Amount : {down_payment_percentage_amount} 
    Down Payment, type {type}: £{loan_amount_result} # What the owner has paid
    Loan Term : Total of {loan_duration} Mortgage Payments
    Total Interst : 
    Mortgage Payoff date : 

    Would you like a more advance version of the mortgage payment system: 
    Y for yes or N for no, type here: """)

    elif down_payment == "£":
        print(f"""Please find the Mortgage results below!
    Home Price : £{home_price}
    Down Payment, type {type2}: 
    Loan Amount : {down_payment_pound_amount}
    Loan Term : 
    Total Interst : 
    Mortgage Payoff date : 

    Would you like a more advance version of the mortgage payment system: 
    Y for yes or N for no, type here: """)

    # Extra - How it works
    how_it_works = input("""What would you like to know
    -
    -
    """)

    # Additional options 
    property_taxes = 0 # As a % or £, ideally a %
    Home_insurance = 0 # As a % or £, ideally a £
    PMI_Insurance = 0 # As a % or £, ideally a £
    HOA_fee = 0 # As a % or £, ideally a £
    Oher_costs = 0 # As a % or £, ideally a £

    # Eventually include - Annual Tax & Cost Increase & Extra Payments
