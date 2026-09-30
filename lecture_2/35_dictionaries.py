def main():
    students={"hermione":"g",
              "harry": "g",
              "ron":"g",
              "dracomf":"s",
              }
    for student in students:
        print(student , students[student])
        print(f"name : {student} house : {students[student]}")


main()
