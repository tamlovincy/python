class Foo:
    
    def __init__(self, name, age ,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def kanchai(self):
        print ("%s,%s岁,%s,上山去砍柴" %(self.name, self.age, self.gender))

    def qudongbei(self):
        print ("%s,%s岁,%s,开车去东北" %(self.name, self.age, self.gender))

    def dabaojian(self):
        print ("%s,%s岁,%s,最爱大保健" %(self.name, self.age, self.gender))


xiaoming = Foo('小明', 10, '男')
xiaoming.kanchai()
xiaoming.qudongbei()
xiaoming.dabaojian()

laoli = Foo('老李', 90, '男')
laoli.kanchai()
laoli.qudongbei()
laoli.dabaojian()
