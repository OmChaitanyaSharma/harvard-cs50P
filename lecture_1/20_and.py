def main():
    # just like we use and in c and c++
    #just instead of using the && we use the litreal word of and here

    score=int(input("enter the grade : "))
    if score >= 90 and score<= 100:
        print("grade : A")
    elif score >= 80 and score< 90:
        print("grade : B")
    elif score >= 70 and score< 80:
        print("grade : C")
    elif score >= 60 and score< 70:
        print("grade : D")
    else:
        print("grade :f you failed boi!!")

main()
