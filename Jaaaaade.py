# python
try:
    iterations = 0
    student_number = 1
    check = True
    print ("Please enter the number of students!")
    number_of_students = int(input())
    while check == True:
        if number_of_students >= 30:
            print(f"Are you sure you want {number_of_students} students? (Y/N)")
            confirm = input()
            if confirm == "Y" or confirm == "y":
                check = False
            else:
                print ("Ok! Let's try again!")
                print ("Please enter the number of students!")
                number_of_students = int(input())
        elif number_of_students == 0:
            print ("There are no students!")
            print ("Please enter the number of students!")
            number_of_students = int(input())
        else:
            print (f"Number of students entered: {number_of_students}")
            check = False

    while True:
         print (f"Please enter the student {student_number}'s' name!")
         student_name = input()
         print ("Please enter the student's score as a whole number!")
         student_grade = int(input())
         if student_grade < 0 or student_grade > 100:
             print ("Please enter a valid score between 0 and 100!")
         else:
             break
         print (f"Name: {student_name}, Grade: {student_grade}")
         iterations = iterations + 1
         student_number = student_number + 1
         if iterations == number_of_students:
                print ("Thank you for entering the student's information!")
                break
print ("Ending Program")
except KeyboardInterrupt:
    print("Exiting Program")
except Exception:
    print("An Error has occured. Error: INVALID DATA TYPE. Please restart the program and use whole numbers when asked to do so")
