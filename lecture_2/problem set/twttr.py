def main():
    name=input("Input: ")

    print("Output: ", end="")
    for char in name:
        if char.lower() not in ["a", "e", "i", "o", "u"]:
            print (char,end="")
    print()


main()
