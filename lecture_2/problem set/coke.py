def main():
    money=50
    while money>0:
        print(f"Amount Due: {money}")
        coin=int(input("Insert Coin: "))
        if coin in [25, 10, 5]:
            money -= coin

    print(f"Change Owed: {abs(money)}")

main()
