def main():
    time=input("time : ")
    side=convert(time)
    if 7<= side <= 8:
        print("breakfast time")
    elif 12<= side <= 13:
        print("lunch time")
    elif 18<= side <=19:
        print("dinner time")


def convert(time):
    hrs, mins=time.split(":")
    hrs=float(hrs)
    mins=float(mins)
    return (hrs+(mins/60))
    


if __name__ == "__main__":
    main()