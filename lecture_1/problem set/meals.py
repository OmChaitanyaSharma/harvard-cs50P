def main():
    clock=input("input time in 24 hours format of hrs:mins : ")
    clock=clock.strip()
    hours=convert(clock)

    if hours>=7 and hours <=8:
        print("breakfast time")
    if hours>=12 and hours <=13:
        print("lunch time")
    if hours>=18 and hours <=19:
        print("dinner time")


def convert(time):
    hours,mins=time.split(":")
    hours=float(hours)
    mins=float(mins)
    hours= hours+(mins/60.0)
    return hours




if __name__ == "__main__":
    main()
