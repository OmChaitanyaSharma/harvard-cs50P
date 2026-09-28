# its better to define main in the starting of the program and then
# then to to call it at the end of the program
def main():
    name=input("enter your name : ")
    hello(name)
    hello()


#and using this method you can define a function after main as well
def hello(name='world'):
    print(f"hello, {name}")
main()
#scope is the area in which a function works
#if somethings are in different scopes then you can use the same name for them
