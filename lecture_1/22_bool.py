def main():
    
    x=int(input("what is the value of x : "))
    if isEven(x):
        print("the number is even")
    else:
        print("the number is odd")

        #bool is basically true and false values that can be assigned to something
        #bool is itself a data type like other data types
        #bool is True and False keep in mind the capital of the lettering of the
        #starting of both true and false


def isEven(num):
    if (num%2==1):
        return False
    else:
        return True


main()
