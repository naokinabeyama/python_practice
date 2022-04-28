
class ClassA:
  def __init__(self, name):
    self.a_name = name

  def print_a(self):
    print("Aクラスのメソッド")
    print("a = {}".format(self.name))
  
  def print_hi(self):
    print("A hi")

class ClassB:
  def __init__(self, name):
    self.b_name = name
  
  def print_b(self):
    print("Bクラスのメソッド")
    print("b = {}".format(self.b_name))
  
  def print_hi(self):
    print("B hi")

class NewClass(ClassA, ClassB):
  def __init__(self, a_name, b_name, name):
    ClassA.__init__(self, a_name)
    ClassB.__init__(self, b_name)
    self.name = name
  
  def print_new_name(self):
    print("name = {}".format(self.name))

  def print_hi(self):
    ClassA.print_hi(self)
    ClassB.print_hi(self)
    print("NewClass hi")

new_class = NewClass("山田", "田中", "佐藤")
new_class.print_a()
new_class.print_b()
new_class.print_new_name()
new_class.print_hi()
