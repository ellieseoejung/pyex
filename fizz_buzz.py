def fizz_buzz(target):
  for i in range(1, target + 1):
      if i % 3 == 0:
          if i % 5 == 0:
              print("FizzBuzz")
          else:
              print("Fizz")
      elif i % 5 == 0:
          print("Buzz")
      else:
          print(i)

fizz_buzz(100)
