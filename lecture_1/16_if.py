def main():
    x=int(input("enter the value of x : "))
    y=int(input("enter the value of y : "))

    if x<y:  # we write if statement like we used to write in c or c++ but just that
         # we dont put the conditions in a bracket and use : at the end of the if
         #statement
        print("y is bigger than x :",y)
    if x>y:
        print("x is bigger than y :",x)
    if x==y:
        print("x is equals to y :" , x)

main()
