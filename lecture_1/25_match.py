def main():
    name=input("what is your name : ")
    name=name.strip()

    #exactly like the switch case in c and c++
    match name:
        case "harry":
            print("griffindor")
        case "hermoine":
            print("griffindor")
        case "ron":
            print("griffindor")
        case "draco":
            print("slytherin")
        case _: # just in case of default case we use an _ in this case
            print("who are you ?")




main()
