def main():

    x=int(input("what is the value of x : "))
    if isEven(x):
        print("the number is even")
    else:
        print("the number is odd")

def isEven(num):
   return True if num % 2 == 0 else False

   #in python you can return something true or false with just one of code and
   #this is a very cool way of returning stuff and things
   
main()
