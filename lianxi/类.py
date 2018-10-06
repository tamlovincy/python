class Foo:
 
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def detail(self):
        print (self.name)
        print (self.age)
 
obj1 = Foo('wupeiqi', 18)
obj1.detail()
print(obj1.name)
print(obj1.age)
