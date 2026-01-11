name = input("Hey! Enter you name: ")

while name == "":
    name = input("Hey! Enter you name: ")


age = int(input("Hello! how old are you: "))

while age < 0:
    print(f"Are you kidding me :( that's impossible.")
    age = int(input("Hello! how old are you: "))

import time
for i in range(3, 0, -1):
    print(i)
    time.sleep(1)

print("\n\n----- (*_*) -----\n\n")


print(f"\n\nHello {name}! Welcome to  the tech world industry.")
print(f"You are {age} years old!")

