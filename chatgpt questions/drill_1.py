def main():
    name=input("enter your name first two letters in messy way may it be spaces after and before it or anything : ")
    name=name.strip().title()
    first, last = name.split()
    print(f"{last}, {first[0]}")
    
main()