from pkg_resources import yield_lines


def outer(max):
  print("開始")
  for i in range(max):
    x = yield i
    print(x)
    print("終了")

a = outer(10)
next(a)
# next(a)
a.send(100)
for i in a:
  print(i)

