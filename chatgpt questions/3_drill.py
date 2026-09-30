def main():
    border=input("select any character you want to be used as a character : ")
    word=input("input the word that you want the character to be placed around : ")
    border=border.strip()
    box_print(word, border[0])
    
def box_print(word ,border='*'):
    print(f"{border} {word} {border}")
    
main()