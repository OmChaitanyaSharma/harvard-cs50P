def main():
    total=float(input("subtotal : "))
    tax=float(input("tax percentage : "))
    final=calculate_total(total, tax)
    print(f"the final amount after taxes is :{final:.2f}")
    
def calculate_total(subtotal, tax_rate):
    amount=subtotal*(tax_rate/100)
    return (amount+subtotal)

main()
    