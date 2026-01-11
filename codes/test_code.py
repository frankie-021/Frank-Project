print("Hello world! Welcome to the python world")
# hello
is_student = True
name = "frank"
age = 21
gpa = 3.8
age = float(age)

if is_student:

    print(f"hello {name}. You are {age} years old. \nAre you a student? {is_student}, Your GPA is {gpa}.")

else:
    print("Sorry! This is only for students") 


print(type(name), "\n", type(age), "\n", type(gpa), "\n", type(is_student)) 