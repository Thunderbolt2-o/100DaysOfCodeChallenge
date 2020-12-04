#Yay it's Day-0️⃣2️⃣ of 100DaysOfCodeChallenge 🥳
#Data Types 😎😎

#Stings:- strings in Python are arrays of bytes representing unicode characters
# "Hello" is a string.
print("Namaste"[0]) # prints the first letter
# The number in the square brackets is the position that we want in the string, and it is called subscripting( in other words indexing). Counting always starts from _zero_
print("Namaste"[6]) #prints the 6th letter

#Integers
print("123" + "100") #make as a single string "123100"
print(123 + 100) #prints adds the both the values as they are not strings 223

# Float:- 3.141

# Boolean True or False

num_char = len("hello")
print(type(num_char)) #this returns the Data type of the variable that we have entered
# 👇👇👇 IMP Dont skip it 👇👇👇
# When we try to concatenate a string with an integer we will get an error and the reason is:-
# In python the + operator after a sequence calls concat with the sequence before the operator and whatever is after the operator. In python string is a sequence. The concat function only works on two sequences of the same type, i.e. two strings or two arrays. In your code you use this operator for string and int.🥱 
# In my words we cant add a Potato🥔 to an apple🍎. 😂😂🤣
# ref:- https://stackoverflow.com/questions/41339372/cant-concatenate-string-with-integer
# we can over come this error with the help of str function

name_char = len(input("what is your name?"))
new_name_char = str(name_char) # converts integer to a string.
# print("Your name has " + name_char + " characters") 👈👈 this statement returs an error as it has differnt datatypes
print("Your name has " + new_name_char + " characters😎😎")
a = float("143")
print(type(a))

#Code exercise add all the numbers of a given number
two_digit_number = input("Enter a two digit number?")
new_two_digit_number = str(two_digit_number) 
print(int(new_two_digit_number[0]) + int(new_two_digit_number[1]))

# Operators

# 3 + 5
# 4 - 2
# 3 * 3
# 3 / 4  always returns float number instead of int
# 3 ** 3 is for powers

# PEMDAS - Left to right
# Priority order
# ()
# **
# * / equal status 
# + -

print(3 * 3 + 3 / 3 - 3)

#Code exercise - 2 make a BMI calculator

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
BMI = int(weight)/(float(height)**2)
print(int(BMI))

# round function also does a similar work as a integer, but it rounds of the decimal place instead of removing the decimal place

numb = 4.565
print(round(numb))
print(int(numb))

# Flow division

print(20 // 3) #returns an int
print(type(20 // 3))
print(20 / 3) # returns a float

#some basic operations 
b = 1
b += 3 # adds 3 to b, this will be similar for other operations too.
# f-strings is used to write the differnt data types in one statement
#To create an f-string, prefix the string with the letter “ f ” ref:- https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/
# Code exercise, How many days, weeks are left in our life if age expection is 90
# Solution
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

new_age = int(age)
years = 90 - new_age
days = years * 365
months = years * 12
weeks = years * 52
print(f"You have {days} days, {weeks} weeks, and {months} months left.")

# Day - 2 project Tip calculator

#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.
bill = float(input("what is the total bill amount ?\n"))
tip = float(input("How much percentage of tip would you like to give ?\n"))
total_people = int(input("Into how many parts should the bill be splited ?\n"))
final_bill = ((tip*bill)/100 + bill)/total_people
final_amount = round(final_bill,2)
print(f"Each person should pay: {final_amount}")
