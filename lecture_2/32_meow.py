def main():
    num=get_number()
    meow(num)

def get_number():
    while True:
        n=int(input("what is the number of times you want the cat to meow : "))
        if n>0:
            return n
def meow(meow):
    for i in range(meow):
        print("meow !")

main()
