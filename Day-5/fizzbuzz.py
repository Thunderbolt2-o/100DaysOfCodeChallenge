for numbers in range(1,101):
  if numbers % 15 == 0:
    print("FizzBuzz") 
  else:
    if numbers % 3 == 0:
      print("Fizz")
    if numbers % 5 == 0:
      print("Buzz")
    else:
      print(numbers)
