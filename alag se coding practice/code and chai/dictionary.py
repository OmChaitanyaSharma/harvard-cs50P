def main():
    tea={"green":"mild", "ginger" : "zesty" , "masala" : "spicy"}
    tea["masala"]="fresh"
    
    for i in tea:
        print (i ,tea[i]) # way one and the easy way to print a dict
        
    for i,j in tea.items(): # way two and the functional way to print a dict
        print(i,j )  # learn how to use .items fucntion while using the dict
        
    for key, values in tea.items(): # way two and this is the same as the way two
        print(key, values)
        
    if "masala" in tea: # using in function while using if 
        print("yes i do possess masala chai")
    
    tea["earl"]="sitrus"
    for key, values in tea.items(): # way two and this is the same as the way two
        print(key, values)
    count=0
    for red,blue in tea.items():
        count=count+1
        print(f"{count}. {red}, {blue}")
        
    tea.pop("ginger") # unlike list this removes the item whose key you have given in it 
    tea.popitem() # this removes the last item like we do in stack or lists 
    count=0
    tea["best tea"] ="ghar ka chai"
    for red,blue in tea.items():
        count=count+1
        print(f"{count}. {red}, {blue}")
    

main()