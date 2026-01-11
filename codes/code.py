

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
                for i in range(5, 0, -1):
                    print(i)
                    time.sleep(1)
                print("\n\nRAMADAN KAREEM!\n\n")

                print("Hello world! Welcome to the python world")

                is_student = True
                name = input(str("Enter your name: \n"))
                age = input("Enter your age: \n")
                gpa = input("Enter your name: \n")
                #age = float(age)

                if is_student:

                    print(f"hello {name}. You are {age} years old. \nAre you a student? {is_student}, Your GPA is {gpa}.")

                else:
                    print("Sorry! This is only for students") 


                print(type(name), "\n", type(age), "\n", type(gpa), "\n", type(is_student)) 
                break

            else:
               print("Error! try again\n") 
        break
    else:
        print("Error! Password does not match.\n")
