def main():
    name=input("camelCase: ")
    for i in name:
        if i.islower():
            print(i,end="")
        else:
            print(f"_{i.lower()}",end="")




main()