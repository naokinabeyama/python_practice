for i in range(1,101):
  if all((i % 3 == 0, i % 5 == 0)):
    print("Fizz Buzz")
  elif i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz")
  else:
    print(i)

# num = 0
# while(num := num + 1) < 101:
#   print(num)

