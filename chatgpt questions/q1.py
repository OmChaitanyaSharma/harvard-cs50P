"""Problem 1: Formal Name Reverser
Write a Python script that prompts the user to enter their full name containing exactly two words (first name and last name) with accidental leading/trailing spaces.

Requirements:

Clean up any leading or trailing whitespace.

Capitalize each name properly (title case).

Split the name into two separate variables: first and last.

Print the name in formal citation order separated by a comma: Last, First (using an f-string).

"""

name=input("enter your name (only two words): ")
name=name.title().strip()
first, last=name.split(" ")
print(f"{last}, {first}")

