from abc import abstractmethod, ABCMeta

class Human(metaclass = ABCMeta):
  def __init__(self, name):
    self.name = name
  
  @abstractmethod
  def say_something(self):
    pass

  def say_name(self):
    print(self.name)

class Woman(Human):
  def say_something(self):
    print("女性: 名前は{}".format(self.name))

m = Woman("aaa")
m.say_something()
