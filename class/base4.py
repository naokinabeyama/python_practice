
class Person: #親クラス

  def __init__(self,name,age):
    self.name = name
    self.age = age
  
  def greeting(self):
    print("Hello {}".format(self.name))
  
  def say_age(self):
    print("{} year old".format(self.age))

class Employee(Person): #子クラス

  def __init__(self, name, age, number):
    super().__init__(name,age)
    self.number = number
  
  def say_number(self): 
    print("my number is = {}".format(self.number))

  def greeting(self): #オーバーライド
    super().greeting()
    print("I\'m employee phone_number {}".format(self.number))

em = Employee("太郎",20,"090-1111-1111")
em.greeting()
em.say_age()
em.say_number()
