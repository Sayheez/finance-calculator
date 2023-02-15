# Create a financial calculator program to calculate two different options either investment calculator or home loan repayment calculator
# This is an example Python program
# The user inputs specific requirements such as principal amount, desired interest rate, expected number of years 
# The program then outputs desired result in monetary value based on the user choice, using a variable, input and if/elif statement

import math


print("Choose either 'investment' or 'bond' from the menu below to proceed: \n")

print("investment - to calculate the amount of interest you'll earn on your investment: ")
print("bond       - to calculate the amount you'll have to pay on a home loan:\n")

user_input = input("Enter your choice of calculation, 'investment' or 'bond':\n")

user_input = user_input.lower()

if user_input == "investment":
    investment_amount = float(input("Enter the amount of money to be deposited: "))
    rate = float(input("Enter the interest rate as a number: "))
    years = int(input("Enter the number of years on investing: "))
    interest = input("Please enter your choice of investment plan: 'simple' or 'compound'").lower()
    if interest == "simple":
        simple_interest = investment_amount * (1 + (rate / 100) * years)
        print(simple_interest)
        print(f"The capital after {years} years of simple interest is {round(simple_interest, 2)}")
    elif interest == "compound":
        compound_interest = investment_amount * math.pow((1 + rate / 100), years)
        print(f"The capital after {years} years of compound interest is {round(compound_interest, 2)}")
elif user_input == "bond":
    current_house_val = float(input("Enter the value of your house: "))
    rate = float(input("Enter the interest rate as a number: "))
    month_rate = (rate / 100 / 12)
    num_of_months = float(input("Enter the number of months to repay the bond: "))

    repayment = (current_house_val * month_rate) / (1 - (1 + month_rate)**(-num_of_months))
    print(f"The amount to be paid each month is {round(repayment, 2)}")
   