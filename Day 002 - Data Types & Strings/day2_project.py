# ----------------------------------------------------------------------------- #
# DAY 2 Project. Tip Calculator.

# Create a greeting for the program.
print("Welcome to the tip calculator.\n")
# Collect all the data required from the user and set their datatypes.
total_bill = float(input("What was the total bill? "))
tip_percentage = float(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))

# Calculate the price with the tip and the price that each person has to pay.
bill_with_tip = round(total_bill * (1+(tip_percentage/100)), 2)
price_per_person = round(bill_with_tip / people, 2)
# Here we use format nomenclature to make sure it always displays 2 decimal 
# digits.
price_per_person = "{:.2f}".format(price_per_person) 

# Print the result.
print(f"Each person should pay: {price_per_person}")
# ----------------------------------------------------------------------------- #
