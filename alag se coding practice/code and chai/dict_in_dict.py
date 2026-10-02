def main():
    
    #using a dict in dict is still as confusinng if not more than using a list
    #in dict
    teastall={"chai":{"masala": "spicy", "herbal":"grassy"},
              "tea":{"redtea":"red","greentea":"mild"}}
    # Loop 1 runs to completion
    for i, j in teastall.items():
        print(i, j)

    # When Loop 1 finishes, j holds the LAST category ('tea')
    
    # Loop 2 runs AFTER Loop 1 is completely finished
    for masala, type in j.items():
        print(masala, type)

main()