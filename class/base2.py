# class Sample():

#   def __init__(self, msg, name):
#       self.msg = msg
#       self.name = name
  
#   def __del__(self):
#     print("削除されました")
#     print(self.name)

#   def print_msg(self):
#     print(self.msg + self.name + "さん")


# sample = Sample("こんにちは", "太郎")
# sample.print_msg()

# del sample


class Sample:

  c_list = []

  def add_c_list(self,data):
    self.c_list.append(data)

print("出力結果:", end=" ")
sample1 = Sample()
sample1.add_c_list("データ1")
print(sample1.c_list)
sample2 = Sample()
sample2.add_c_list("データ2")
print(sample2.c_list)

for item_data in sample1.c_list:
  print(item_data, end=" ")
