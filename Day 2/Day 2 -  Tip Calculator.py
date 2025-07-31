# Day 2 Project - Tip Calculator

print("Welcome to the Tip Calculator!")

# Get the bill amount
bill = float(input("What was the total bill? $"))

# Get the tip percentage
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

# Get number of people
people = int(input("How many people to split the bill? "))

# Calculate tip amount
tip_amount = bill * (tip_percentage / 100)

# Calculate total bill including tip
total_bill = bill + tip_amount

# Calculate amount per person
bill_per_person = total_bill / people

# Round to 2 decimal places
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")