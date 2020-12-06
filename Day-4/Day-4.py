# Yay it's the Day-0️⃣4️⃣ of the challange. Today I am going to learn python lists and randomizaton 🤪
import random
# import my_module 
# this statement is used to import a module,
# What is a module, in simple words it a function that is used to do some extra things without typing that extra lines of code 😎
# Ref website for modules https://www.askpython.com/
random_integer = random.randint(1,10)
print(random_integer)
# print(my_module.pi) # this my reference module

random_float = random.random()

random_float_number = 5*random.random() #Generates random numbers between 0 to 5 😉
print(random_float_number)

# Random_love_score generator

love_score = random.randint(1, 100) # generates a random number between 1 to 100

print(f"Your love score is {love_score}")

# Code exercise Head's or tails 

number = round(random.random())

if number == 1:
 print("Heads")
if number == 0:
 print("Tails")

# Lists 🤠

states = ["Andhra pradesh", "Manipur", "Maharastra"]

print(states[1])
# we can also give negatve numbers as the position -1 gives last number

# Editing lists
# Change any thing in the list
states[1] = "Goa"

print(states[1])

# ref for the lists documentation https://docs.python.org/3/tutorial/datastructures.html

# Code exercise, Who should pay the bill

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
import random
#Write your code below this line 👇
list_size = len(names)
random_number = random.randint(0,list_size-1)
print(f"{names[random_number]} is going to buy the meal today!")
print(random_number)

# Code exercise, Hide the treasure
# give an input of 2 digit number  between 1,1 and 3,3 => 11 or 12 or 13 or 23 <= examples
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

position_1 = int(position[0])
position_2 = int(position[1])
map[position_1 - 1][position_2 - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")

# Code exercise who is going to pay the bill

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
import random
#Write your code below this line 👇
list_size = len(names)
random_number = random.randint(0,list_size)
print(f"{names[random_number]} is going to buy the meal today!")
print(random_number)
