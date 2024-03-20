import math

# This is my first Python CAPSTONE PROJECT This project will ask a user for
# to choose a one of two financial calculator,either investment or bond
# repayment. The choice of calculator will further ask for user to enter info
# such as interest rate, simple or compound interest, term/period, capital
# amount, present value the program will then calculate the values and return
# the answer on screen

print("investment - to calculate the amount of interest you'll earn on your "
      "investment")
print("bond - to calculate the amount you'll have to pay on a home loan")
# Ask the user to enter choose between the two calculators
calculator_choice = input("Enter either 'investment' or 'bond' from the menu "
                          "above to proceed: ")
# if choice of calculator is investment proceed
if calculator_choice.lower() == 'investment':
    # ask the user to enter capital amount, interest rate, number of years,
    # choose simple or compound interest
    capital_amount = float(input("Please enter your deposit amount: "))
    interest_rate = float(input("Please enter interest rate, just the number "
                                "i.e 8 not 8%: "))
    num_years = int(input("Please enter number of years you plan to invest: "))
    interest = input("Please enter the type of interest you want, write only "
                     "simple or compound: ")

    # calculate the final amount and based on type of interest
    if interest.lower() == 'simple':
        final_amount = round(
            capital_amount * (1 + (interest_rate / 100) * num_years), 2)
        print(
            f"Your R{capital_amount} after {num_years} years at "
            f"{interest_rate}% will be R{final_amount}")
    elif interest.lower() == 'compound':
        final_amount = round(
            capital_amount * math.pow(1 + (interest_rate / 100), num_years), 2)
        print(
            f"Your R{capital_amount} after {num_years} years at "
            f"{interest_rate}% will be R{final_amount}")
# if calculator of choice is bond proceed
elif calculator_choice.lower() == 'bond':
    # ask the user to enter present value, interest rate, term in
    # months/number of months
    present_value = float(input("Please enter the present value: "))
    interest_rate = float(input("Please enter interest rate, only number i.e "
                                "8 not 8%: "))
    num_months = int(input("Please enter the number of months you plan to pay "
                           "off your bond i.e 10yr = 120 months: "))

    # calculate the monthly repayments and display on screen
    monthly_repayments = (
            ((interest_rate / 1200) * present_value) /
            (1 - (1 + (interest_rate / 1200)) ** (-num_months)))

    monthly_repayments = round(monthly_repayments, 2)
    print(f"Monthly repayments for a bond of R{present_value} at "
          f"{interest_rate}% for a period of {num_months} months"
          f"is R {monthly_repayments}")
# if the choice is invalid, print error message
else:
    print(
        "Sorry, you did not enter a valid calculator. Try again later, "
        "and only enter investment or bond")
