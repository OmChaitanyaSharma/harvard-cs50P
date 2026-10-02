def main():
    name=input("camelCase: ")


    print("snake_case: ", end="")
    for char in name:
        if char.isupper():
            print(f"_{char.lower()}",end="")
        else:
            print(f"{char}",end="")

    print()




main()
