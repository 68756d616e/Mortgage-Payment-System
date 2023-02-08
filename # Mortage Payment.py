# Mortgage payment system

while True:

    house_price = int(input("Please input the amount of the house £"))
    loan_term = int(input("Please input the duration of the loan term: "))
    
    type = "£"
    type2 = "%"
    
    down_payment = input("""Please choose an option A or B!
A - A specific amount in GBP £
B - A percentage """)

    if down_payment == "A" or down_payment == "a":
        print("You chose A, a specific amount")
        down_payment_pound = int(input("Please enter the amount of the down peaymnt £"))
        
        loan_amount = house_price - down_payment_pound
        amount_payments = 12 * loan_term
        interest_rate = float(input("Please enter the interest rate as a decimal, example 2.5 : "))
        interest_amount = interest_rate * 0 # I need to create an interest rate 
        payment_amount = loan_amount + interest_amount

        print(f"""
Home Price : {house_price}
Loan Amount, type GBP {type} : {loan_amount}
Down Payment : {down_payment_pound}
A total of {amount_payments} Mortgage Payments :  {payment_amount} # This will change once the interest rate has been created
Total Interest : 
Mortgage Pay Off :
        """)
        
    elif down_payment == 'B' or down_payment == 'b':
        print("You chose a percentage")
        down_payment_percentage = float(input("Please enter the percentage amount %"))

        loan_amount = house_price - down_payment_pound
        amount_payments = 12 * loan_term
        interest_rate = float(input("Please enter the interest rate as a decimal, example 2.5 : "))
        interest_amount = interest_rate * 0 # I need to create an interest rate 
        payment_amount = loan_amount + interest_amount
                
        print(f"""
Home Price : {house_price}
Loan Amount, type GBP {type2} : {loan_amount}
Down Payment : {down_payment_pound}
A total of {amount_payments} Mortgage Payments :  {payment_amount} # This will change once the interest rate has been created
Total Interest : 
Mortgage Pay Off :
        """)

    else:
        print("Please choose A or B")

    # Additional options 
    property_taxes = 0 # As a % or £, ideally a %
    Home_insurance = 0 # As a % or £, ideally a £
    PMI_Insurance = 0 # As a % or £, ideally a £
    HOA_fee = 0 # As a % or £, ideally a £
    Oher_costs = 0 # As a % or £, ideally a £

    # Eventually include - Annual Tax & Cost Increase & Extra Payments
