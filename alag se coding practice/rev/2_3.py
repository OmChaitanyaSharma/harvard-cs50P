def main():
    type=input("Input: ")
    print("Output: ",end="")
    for i in type:
        if not i.lower() in ["a","e","i","o","u"]:
            print(i,end="")
    print()
main()