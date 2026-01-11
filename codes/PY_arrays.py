# LIST []    =  mutable and most flexible.
# TURPLE ()  =  immutable, faster.
# SET  {}    =  mutable (add/remove), unordered.
#               NO dublicates, best for membership testing.



#          LIST []
print("\n                     LIST [] \n")
#fruits = ["orange", "banana", "mango","apple","strawberry"]
#fruits[0] = "pineappple"
#fruits.append("coconut") 
#fruits.remove("banana")
#fruits.pop(4)
#fruits.sort()
#fruits.reverse()
#fruits.insert(2, "blueberry")
#fruits.count(2)
#print("\n\n\n")
#print(f"the selected fruit(s) is/are {fruits}")


# Example: List input from user

# Ask user for input
'''
pillars = ["sahadah", "prayers", "zakat", "ramadan", "hajj"]
while 1:
    data = input("Enter the pillars of Islam (separated by spaces): ")
    # Convert input string to list
    my_list = data.split()
    if my_list == pillars:
        print("\nThe pillars of Islam are: ", my_list)
        break
print("\n\n\n")






#         TURPLE ()
print("\n                     TURPLE () \n")

# Unlike LIST, when TURPLES are assigned, they cannot be changed. But they're faster.
#study = ("book", "pen", "pencil","ruler","rubber")
#print(f"You need {study} to prepare for studies") 


dataP = input("Enter the pillars of faith in Islam (separated by spaces)\n")
data_turple = tuple(dataP.split())
print("They are ", data_turple )
print("\n\n\n")






'''
#         SET {}
print("\n                     SET {} \n")
#Sets also do not support item assignment aside from ADD/REMOVE. They are not also arrange in order.
#study = {"book", "pen", "pencil","ruler","rubber"}
#study.add("papers")
#study.remove("rubber")
#print(f"You need {study} to prepare for studies\n") 


dataS = input("Enter the name of the 10 sahaba that were promise Jannah in their life time:  ")
data_set = set(dataS.split())
print("Their names are:\n ", data_set)
    