def fizzbuzz(num):
  if number % 3 == 0 and number % 5 == 0:
      print("Fizz Buzz")
  elif number % 3 == 0:
      print("Fizz")
  elif number % 5 == 0:
      print("Buzz")

number = int(input("Pick a number! "))
fizzbuzz(number)