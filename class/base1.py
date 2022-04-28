class SampleA():
  class_val = "クラス val"

  def set_val(self):
    self.instance_val = "インスタンス val"

  def print_val(self):
    print("クラス変数 = {}".format(self.class_val))
    print("インスタンス変数 = {}".format(self.instance_val))

instance_a = SampleA()
instance_a.set_val()
instance_a.print_val()
print(instance_a.class_val)
print(instance_a.__class__.class_val)
print("-" * 50)
instance_b = SampleA()
instance_b.set_val()
instance_b.print_val()
print("-" * 50)
instance_a.__class__.class_val = "クラス バル"
print(instance_a.class_val)
instance_a.print_val()
instance_b.print_val()
