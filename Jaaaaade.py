try:
    iterations = 0
    student_number = 1
    check = True
    print("Please enter the number of students!")
    number_of_students = int(input())
    
    # Validate the number of students input
    while check == True:
        if number_of_students >= 30:
            print(f"Are you sure you want {number_of_students} students? (Y/N)")
            confirm = input()
            if confirm == "Y" or confirm == "y":
                check = False
            else:
                print("Ok! Let's try again!")
                print("Please enter the number of students!")
                number_of_students = int(input())
        elif number_of_students == 0:
            print("There are no students!")
            print("Please enter the number of students!")
            number_of_students = int(input())
        else:
            print(f"Number of students entered: {number_of_students}")
            check = False

    # Loop for entering each student's name and score
    while iterations < number_of_students:
        print(f"Please enter the student {student_number}'s name!")
        student_name = input()
        print("Please enter the student's score as a whole number!")
        
        try:
            student_grade = int(input())
            # Validate grade
            if student_grade < 0 or student_grade > 100:
                print("Please enter a valid score between 0 and 100!")
                continue
        except ValueError:
            print("Invalid input for grade! Please enter a whole number.")
            continue

        print(f"Name: {student_name}, Grade: {student_grade}")
        iterations += 1
        student_number += 1

    print("Thank you for entering the students' information!")
    print("Ending Program")

except KeyboardInterrupt:
    print("Exiting Program")
except Exception as e:
    print(f"An error has occurred. Error: {e}. Please restart the program and use whole numbers when asked to do so.")
