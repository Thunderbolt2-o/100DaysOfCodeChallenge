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
