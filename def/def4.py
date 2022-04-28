
# def print_hello():
#   print("hello")

# def print_goodbye():
#   print("goobye")

# var = [1, 2, print_hello, print_goodbye]

# var[2]()
# var[3]()

def hello_world(a):
  print("{} wold".format(a))

def hello():
  print("こんにちは")

def hello_hello(b):
  b("hello")
  return hello

var = hello_hello(hello_world)
var()
