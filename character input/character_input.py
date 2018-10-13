print("CHARACTER INPUT\n\nCreate a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.\n")

import datetime
date = datetime.datetime.now()
print("The year is",str(date.year)+".\n") # TEST

user_name = input("What is your name? ")
while True: # name validations
    if user_name.isalpha():
        break
    elif user_name == "": 
        user_name = input("Please enter your name. ")
    else:
        user_name = input("Please only use letters when entering your name. ")

user_age = input("How old are you? ")
while True: # name validations
    if user_age.isdigit():
        if int(user_age) == 0: 
            user_age = input("Please enter an age above 0. ")
        else:
            break
    elif user_age == "": 
        user_age = input("Please enter your age. ")
    else:
        user_age = input("Please only use positive integers when entering your age. ")

print("\nYour name is",user_name,"and you are",str(user_age),"years old.") #TEST
if int(user_age) < 100:
    print(user_name+", in",str(date.year+(100-int(user_age))),"you will be 100 years old.")
elif int(user_age) > 100:
    print(user_name+", you are over 100 years old. You turned 100 in",str(date.year-(int(user_age)-100))+".2")
else:
    print(user_name+", you are already 100 years old.")
print("\nEnd program.")
