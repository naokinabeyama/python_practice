class Human:

  class_name = "Human"

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def print_name_age(self):
    print("名前 = {}, 年齢 = {}".format(self.name,self.age))

  @classmethod
  def print_class_name(cls, msg):
    print(cls.class_name)
    print(msg)

  @staticmethod
  def print_msg(msg):
    print(msg)


Human.print_class_name("こんにちは")
man = Human("太郎", 18)
man.print_name_age()

