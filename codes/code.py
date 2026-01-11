

while(1):
    password = input(str("Create a password\n"))
    comPassword = input(str("Comfirm your password\n"))

    if(password == comPassword):
        print("\n\n Password successfully created!\n\n")
        print("\n\n ----- LOGIN ----- \n\n")

        while(1):
            login = input(str("Enter your password\n"))

            if(password == login):
                print("Login successfully!\n")

                import time
                for i in range(3, 0, -1):
                    print(i)
                    time.sleep(1)
                print("\n\n--- WELCOME! ---\n\n")

                print("Welcome to the python world")


                is_student = input("Are you a student(yes/no)? ")
                
                if is_student == "yes":

                    name = input(str("Enter your name: \n"))
                    age = input("Enter your age: \n")
                    mark = int(input("Enter your grade in percentage: \n"))
                    gpa = (mark/100) * (4)
                    gpa = float(gpa)
                    #age = float(age)

                    print(f"hello {name}. You are {age} years old. Your GPA is {gpa}.")

                else:
                    print("Sorry! This is only for students") 

                print("\n\n", type(name), "\n", type(age), "\n", type(gpa), "\n", type(is_student)) 
                break

            else:
               print("Invalid! try again\n") 
        break
    else:
        print("Error! Password does not match.\n")
