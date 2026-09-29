"""
Write a Python script that calculates how much each person owes on a restaurant bill.Requirements:Prompt the user for:The total bill amount (as a floating-point number).The tip percentage to add (as an integer, e.g., 15 for 15%).The number of people splitting the bill (as an integer).Calculate the total bill including the tip: $\text{Total} = \text{Bill} \times (1 + \frac{\text{Tip}}{100})$.Divide the total by the number of people.Print the amount each person should pay, formatted strictly to 2 decimal places with a dollar sign $ in front (using f-string formatting).
"""

bill=float(input("enter the total bill :"))
tip=float(input("enter the tip percentage "))
number=float(input("enter the number of people seating at the table "))

total=bill*(1+(tip/100))
bpp=total/number

print(f"every person needs to pay ${bpp:.2f}")