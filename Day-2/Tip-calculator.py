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
