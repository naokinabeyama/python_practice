import sys

list_a = [i for i in range(10000)]

def num(a):
  i = 0
  while i < a:
    yield i
    i += 1

a = num(10000)
print(sys.getsizeof(list_a))
print(sys.getsizeof(a))
