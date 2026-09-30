def main():
    x=int(input("what is the value of x : "))
    isEven(x)

def isEven(num):
    if (num%2==1):
        print("odd number ")
    else:
        print("even number ")


main()
