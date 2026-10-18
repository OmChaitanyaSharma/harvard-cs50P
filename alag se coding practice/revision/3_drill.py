def main():
    due=75
    while due>0:
        
        print("amount due: ", due)
        coin = int(input("Insert coin: "))
        
        if coin in [10,20,50]:
            due= due-coin        

    print("change owed :",abs(due))
        
main()