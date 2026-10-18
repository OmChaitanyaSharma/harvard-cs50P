def main():
    amount=50
    while amount>0:
        print("Amount Due :",amount)
        coin=int(input("insert coin : "))
        
        if coin in [25,10,5]:
            amount = amount -coin
        continue
            
    
    print ("Change owed :",abs(amount))
main()

