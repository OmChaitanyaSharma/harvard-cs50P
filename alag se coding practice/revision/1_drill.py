def main():
    tag=input()
    if validate_tag(tag):
        print("valid")
    else:
        print("invalid")
def validate_tag(t):
    for i in range(len(t)):
        if t[i].isdigit():
            if t[i]=="0":
                return False
            if not t[i:].isdigit():
                return False
            break
    return True
        
    
    
main()