num = 10
print(num)
num_str = str(num)
num_list = [num_str, "20", "30"]
num_list.append("40")
num_tuple = tuple(num_list)
print(num_tuple)
a = input()
num_tuple += (a,)
print(num_tuple)
num_set = {"40", "50", "60"}
print(set(num_tuple) | num_set)

num_dict = {num_tuple: num_str}
for k,v in num_dict.items():
  print(k,v)

print(len(num_list))

print(num_dict.get("MyKey", "Does not exist"))

num_list.extend(["50", "60"])
print(num_list)
num = int(input())
if num < 50:
  is_under_50 = True
else:
  is_under_50 = False

print(is_under_50)

print("num_str = {}".format(num_str))
print(dir(num_dict))
