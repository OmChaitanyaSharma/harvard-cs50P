def main():
    name=input("Input: ")
    print("Output: ",end="")
    for i in name:
        if i.lower() not in ["a","e","i","o","u"]:
            print(i,end="")
main()
            
    
    
    