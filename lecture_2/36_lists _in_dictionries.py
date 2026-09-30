def main():
    students=[
        {
            "name" : "her" , "hoiuse" : "GR" , "pat" : "otter"
        },
        {
            "name" : "ron" , "hoiuse" : "GR" , "pat" : "weasel"
        },
        {
            "name" : "harry" , "hoiuse" : "GR" , "pat" : "stag"
        },
        {
            "name" : "draco" , "hoiuse" : "SLY" , "pat" : None
        }
    ]

    for student in range(len(students)):
        print(student+1 , students[student]["name"],students[student]["hoiuse"],students[student]["pat"],sep=" ,")
        #a little confused about how this is printed and how this is to be used

    for student in students:
        print(student["name"], student["hoiuse"], student["pat"], sep=" ,")
        #i am printing them using two types of types of codes

        # so basically
        """
        The variable students represents your entire list containing all of the dictionaries.When you write for student in students:, Python extracts one item from that list at a time and assigns it to the temporary loop variable student. Because the items inside your list are dictionaries, student becomes that specific individual dictionary for that single loop iteration.
        """


main()
