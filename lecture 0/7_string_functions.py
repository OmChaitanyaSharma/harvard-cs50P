name=input("enter your name? ")
name2=name
name3=name

#remove whitespaces from between the strings

name = name.strip()  #strip function removes whitespaces from the strings
name = name.capitalize()  # this function makes the first letter capital
name2 =name2.title() # this function makes the first letter of all the words
name3= name3.strip().title() # strip and capitalize


print(f"hello , {name}")
print(f"hello , {name2}")
print(f"hello , {name3}")
