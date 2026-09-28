# a float also known as floating point value
# its a number with a decimal value


x=float(input("input a number x :"))
y=float(input("input  a number y :"))
z=x+y
print(f"{z:,}")  #if you write like this you can put commas in american number system


#round function can round off a number
z=round(z)
print(f"{z:,}")

r=round(x/y, 2)
print(f"{r:.2f}") # here like we use .2f we will print the last two digits after the
# decimal point only as we do in c and java or any printf line 
