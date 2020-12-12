# Yay! it's Day - 1️⃣0️⃣ 😎 Today I am going to learn about dictionaries in python

programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again."
}

print(programming_dictionary["Bug"])

# adding new items to the dictionary

programming_dictionary["Loop"] = "The action of doing something ou=vetrt and over again"

print(programming_dictionary)

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
# Scores 91 - 100: Grade = "Outstanding"

# Scores 81 - 90: Grade = "Exceeds Expectations"

# Scores 71 - 80: Grade = "Acceptable"

# Scores 70 or lower: Grade = "Fail"

student_grades = {

}

#TODO-2: Write your code below to add the grades to student_grades.👇

for student in student_scores:
  score = student_scores[student]
  if score > 90:
    student_grades[student] = "Outstanding"
  elif score > 80:
    student_grades[student] = "Exceeds Expectations"
  elif score > 70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)
