# Yay!! it's Day - 0️⃣5️⃣, five days have completed just like a snap😜. I will just keep going. Today I am going to learn main things of any programming language they are loops

# for loop
fruits = ["apple", "peach", "pear"]
for fruit in fruits:
  print(fruit)
  print(fruit + " pie")
  # Intendation is the most important thing
print(fruits)

# for loop 
# range function it returns a sets of specified number ex: - range(0,100) retruns numbers from 0 to 99
# And range(0,100,3) will give numbers with space 3 between them

for number in range(1,10):
 print(number)

total = 0
for numbers in range(1,101):
  total += numbers
print(total)

even_sum = 0
for numbers in range(1,101):
  if numbers % 2 == 0:
    even_sum += numbers
print(even_sum)

# Code exercise average of the heights

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
t_height = 0
n = 0
# 156 178 165 171 187
# 180, 124, 165, 173, 189, 169, 146
#Write your code below this row 👇
for height in student_heights:
  t_height += height
  n += 1
new_avg_height = round(t_height/(n)) 

print(new_avg_height)

# Code exercise Max score

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

max_score = 0
for score in student_scores:
  if score > max_score:
   max_score = score  
print(max_score)
