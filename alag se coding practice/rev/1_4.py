word=input("x y z : ")
x,y,z=word.split(" ")
x=float(x)
z=float(z)
result=0

match y:
    case "+":
        result=x+z
    case "-":
        result=x-z
    case "*":
        result=x*z
    case "/":
        result=x/z
    case _:
        result=0
print(f"{result:.1f}")