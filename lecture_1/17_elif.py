def main():
    x=int(input("enter the value of x : "))
    y=int(input("enter the value of y : "))

    if x<y:
      print("y is bigger than x :",y)
    elif x>y:
        print("x is bigger than y :",x)
    elif x==y:
        print("x is equals to y :" , x)
        # we use if elif as else if ,if the first statement is not true
        # then and only then we use the next elif statement 

main()