# Yay it's the day:- 0️⃣3️⃣ just super exited to learn conditionals and scopes today 🥳
# Are you upto the height ?? 😜
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  # this is  the syntax for the if else statement in the python 
  # :: if (condition):
    #   statements
    #  else:
    #   statements
  print("You can ride the rollercoaster!. Have fun 😎 😎")
else:
  print("Sorry, ypu have to grow taller before ypu can ride.🥴 🥴")

  # comparison operators 🙄🙄
  # > Greater than
  # < less than
  # = assignment operator
  # == to check equality
  # <= less than or equal to
  # >= greater than or equal to
  # != not equal to 

# Code exerice odd or even

# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
if number % 2 == 0 :
# "%" symbol is use to give the remainder
  print("This is an even number.")
else:
  print("This is an odd number.")  

# Nested if/else statement

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  age = int(input("What is your age? "))
  if age < 12:
   print("Please pay 50 ruppees")
  elif age <= 18 :
   print("please pay 80 ruppees")
  else:
   print("Please pay 100 ruppees.")
   print("You can ride the rollercoaster!. Have fun 😎 😎")
else:
  print("Sorry, ypu have to grow taller before ypu can ride.🥴 🥴")

# BMI Calculator Version 2.o


height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi =round(weight/height**2)
  
if bmi <= 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi > 18.5 and bmi <= 25 :
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi > 25 and bmi <= 30 :
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi > 30 and bmi <= 35 :
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")


# Leap year calculator


year = int(input("Which year do you want to check? "))

# logic 🙄
# if year is divisible by 400 then is_leap_year
# else if year is divisible by 100 then not_leap_year
# else if year is divisible by 4 then is_leap_year
# else not_leap_year

if year % 400 == 0:
 print("leap year.")
elif year % 100 == 0:
  print("Not leap year.")
elif year % 4 == 0:
  print("leap year.")
else:
  print("Not leap year.")

# Roller coster version 3 LOL 🤣🤣😂

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  age = int(input("What is your age? "))
  if age < 12:
   bill = 50
   print("Child ticket cost is 50 ruppees")
  elif age <= 18 :
   bill = 80
   print("Youth ticket cost is 80 ruppees")
  else:
   bill = 80
   print("Adult ticket cost is 100 ruppees.")

  wants_photo = input("Do you need a photo taken? Y or N ")
  if wants_photo == "Y":
    bill += 30
    print(f"Your total bill is {bill}")
  else:
    print(f"Your total bill is {bill}")
  print("You can ride the rollercoaster!. Have fun 😎 😎")
else:
  print("Sorry, ypu have to grow taller before ypu can ride.🥴 🥴")

# Code exercise Pizza bill calculator 


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

cost = 0

if size == "S":
  cost = 15
  if add_pepperoni == "Y":
   cost += 2
  if extra_cheese == "Y":
   cost += 1
  print(f"Your final bill is {cost}")
else:
  if size == "M":
   cost = 20
  if size == "L":
   cost = 25
  if add_pepperoni == "Y":
   cost += 3
  if extra_cheese == "Y":
   cost += 1
  print(f"Your final bill is ${cost}")

# Operators "and, or , not"
# and all conditions should be true
# or any one condition is true
# reverse the contition 
# Lol I have used the operators in the code before it self 🤣🤣

# Love calculator 
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

low_name1 = name1.lower()
low_name2 = name2.lower()
print(low_name1)
t_count = low_name1.count("t") + low_name2.count("t")
r_count = low_name1.count("r") + low_name2.count("r")
u_count = low_name1.count("u") + low_name2.count("u")
e_count = low_name1.count("e") + low_name1.count("e")

true_total = t_count + r_count + u_count + e_count

l_count = low_name1.count("t") + low_name2.count("l")
o_count = low_name1.count("r") + low_name2.count("o")
v_count = low_name1.count("u") + low_name2.count("v")
e1_count = low_name1.count("e") + low_name1.count("e")

love_total = l_count + o_count + v_count + e1_count

total_count = int(f"{true_total}{love_total}")
print(total_count)

# ref:- https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/
# ref:- https://www.geeksforgeeks.org/python-string-count/
# For Love Scores less than 10 or greater than 90, the message should be:

# "Your score is **x**, you go together like coke and mentos."

# For Love Scores between 40 and 50, the message should be:

# "Your score is **y**, you are alright together."

# Otherwise, the message will just be their score. e.g.:

# "Your score is **z**."

if total_count < 10 or total_count > 90:
  print(f"Your score is {total_count}, you go together like coke and mentos.")
elif total_count > 40 and total_count < 50 :
  print(f"Your score is {total_count}, you are alright together.")
else:
  print(f"Your score is {total_count}.")
