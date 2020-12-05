print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


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
