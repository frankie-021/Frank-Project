"""print(f"Your name is {name}")

print(f"Your age is {age}\n\n")

if age > 18:
    print("You are an adult. You have the rights to vote for the coming elections.")
elif age < 0:
    print("Invalid! Are you kidding me :( ")
else:
    print("You are still a child. you are not eligible to vote for the comming elections.") """




is_raining = False
temp = int(input("Enter the temperature in degree celsius: "))

if temp > 35 or temp < 0 or is_raining:
    print("Plz stay indoors, the temperature is not favourable.")
else:
    print("You are safe to go outdoor")