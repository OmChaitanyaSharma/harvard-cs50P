def main():
    num=input("write in format of x + y : ")
    num=num.strip()
    x,y,z=num.split(" ")

    x=float(x)
    z=float(z)


    match y:
        case "+":
            v=x+z
        case "-":
            v=x-z
        case "/":
            v=x/z
        case "*":
            v=x*z


    print(f"{v:.1f}")

main()
