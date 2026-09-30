def main():

    num=int(input('how many number of times do you want the cat to meow : '))

    while num<0:
        num=int(input('number of meows cannot be negative so try again  '))


    for i in range(num): #way two of writing loop in python is with range
        print("MEOW! \n")



main()
