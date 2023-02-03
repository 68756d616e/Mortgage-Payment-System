# Mortage Payment

# Welcome message
print("Welcome to a mortage payment system")

# Basic version

# Mortage calculator
# Home price & what is a home price
home_price = int(input("Please enter the amount of the mortgage £"))

# Down payment & what is a down payment
down_payment = input("Please choose a % or £")
if down_payment == 'Percentage %':
    percentage_amount = float(input("Please enter the amount of the percentage as a decimal. Example 0.2 :"))
    type = '%'
elif down_payment == "£":
    pound_amount = float(input("Please enter the amount the pound :"))
    type2 = 'GBP £'
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
down_payment_result = percentage_amount * home_price
loan_amount_result = home_price - down_payment_result

# Loan Term calculation
loan_duration = 12 * loan_term  # The amount of mortgage payments

# Loan Amount
loan_amount_result = home_price - loan_amount_result

# Result
if down_payment == "%":
    print(f"""Please find the Mortgage results below!
Home Price : £{home_price}
Loan Amount : laon_amount_result
Down Payment, type{type}: £{loan_amount_result}
Loan Term : Total of {loan_duration} Mortgage Payments
Total Interst : 
Mortgage Payoff date : 

Would you like a more advance version of the mortgage payment system: 
Y for yes or N for no, type here: """)

elif down_payment == "£":
    print(f"""Please find the Mortgage results below!
Home Price : £{home_price}
Down Payment, type{type2}: 
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
