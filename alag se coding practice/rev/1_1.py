def main():
    number=input("what is the answer to the Great Question of Life, the Universe, and Everything.")
    number= number.strip().lower()
    if number=="42":
        print("Yes")
    elif number=="forty-two":
        print("Yes")
    elif number=="forty two":
        print("Yes")
    else:
        print("No")
main()