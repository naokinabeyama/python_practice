# import re

# prog = re.compile("(K|S)u(r|s)(a|o)nf?(a|o)(o|m)gi?(saya)?", re.IGNORECASE)
# print(prog)
# ret = prog.search("suranamg")
# print(ret[0])


# a = {"dog","cat","tiger","elephant"}
# b = {"kaeru","cat","ti-ta","manmosu"}

# print(a - b)

# date = {x:y**2 for y in range(2,10) for x in ["A","B","C"] if y**2 % 3 == 0}
# print(date)


# def scope_test():
#   spam = "test spam"
#   def do_local():
#     spam = "local spam"
#     print(spam)

#   def do_nonlocal():
#     nonlocal spam
#     spam = "nonlocal spam"
  
#   def do_global():
#     global spam
#     spam = "global spam"
  
#   do_local()
#   print("do_localの値は:", spam)
#   do_global()
#   print("do_globalの値は:", spam)
#   do_nonlocal()
#   print("do_nonlocalの値は:", spam)

# scope_test()
# print("In global scope", spam)


# import textwrap

# a = "aiueokakakakakakkakakak"

# print(textwrap.wrap(a,width=3))

# data = list([x**2 for x in range(10)])
# print(data)

# list_a = []
# for i in range(10):
#   list_a.append(i**2)

# print(list_a)


# a = list(map(lambda x:x**2, range(10)))
# print(a)


# from collections import deque

# pref = deque(["Tokyo", "Osaka", "Fukuoka"])
# pref.append("Mie")
# pref.append("Ehime")
# pref.popleft()
# print(pref)

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# power = [[row[i] for row in matrix] for i in range(3)]
# print(power)

# a = list(zip(*matrix))
# print(a)

# f = ["apple", "kiwi", "plum"]
# for i in f[:]:
#   print(i)
#   if len(i) < 5:
#     f.insert(0,i)
#     print(f)
#     f.pop()
#     print(f)



# from collections import Counter, deque
# print("abcdavccefgga")
# a = "aabcdavccefgga"
# b = Counter(a)
# print(b)


# print("PHP" < "Perl" < "python")

# val = "abc"
# print(val.rjust(5, "+"))

# matrix = [[1,2,5],[4,9,25],[8,27,125]]

# power = [[row[i] for row in matrix] for i in range(3)]
# print(power)

# power2 = list(zip(*matrix))
# print(power2)

# print((1,2,5) < (1,2,5,-1))

# import math

# print(math.pow(2,3))
# print(2**3)

# from collections import deque

# pref = deque(["tokyo", "osaka", "fukuoka"])
# print(pref)


# a = set('americansprit')
# print(a)

# b = 'americansprit'
# print(b[:100] + 'j')

# print((10,20) != (10.0,20.0))

print(17 % 3)
