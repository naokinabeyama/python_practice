from abc import abstractmethod, ABCMeta

class Animals(metaclass=ABCMeta):
  @abstractmethod
  def speak(self):
    pass

class Dog(Animals):
  def speak(self):
    print("わん")

class Cat(Animals):
  def speak(self):
    print("にゃー")

class Sheep(Animals):
  def speak(self):
    print("めー")

class Other(Animals):
  def speak(self):
    print("そんな動物はいない")


num = int(input("1 ~ 3を入力してください"))

if num == 1:
  animal = Dog()
elif num == 2:
  animal = Cat()
elif num == 3:
  animal = Sheep()
else:
  animal = Other()

animal.speak()
