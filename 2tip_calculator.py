

print("Welcome to the tip calculator.")

# Get the total bill from the user
total = float(input("What was the total bill? "))

# Get the tip percentage from the user
print("What percentage tip would you like to give? 10, 12, or 15?")
percentage = float(input())

# Check if the entered percentage is valid
if percentage in [10, 12, 15]:
    # Get the number of people
    people = int(input("How many people to split the bill? "))

    # Calculate the tip and total per person
    tip_amount = total * (percentage / 100)
    total_with_tip = total + tip_amount
    per_person_share = total_with_tip / people

    # Display the result
    print(f"Each person should pay: {per_person_share:.2f}")
else:
    print("Please enter a valid tip percentage (10, 12, or 15).")