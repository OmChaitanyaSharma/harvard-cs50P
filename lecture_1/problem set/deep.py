def main():
    question=input("what is the answer to the greatest question in life Great Question of Life, the Universe and Everything : ")
    question=question.strip().lower()
    match question:
        case "42" | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")
main()
