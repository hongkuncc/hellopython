#encoding:utf-8
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return "Person(%s)"%self.name
    def __repr__(self):
        return "Person(%s)"%self.name

p1=Person('chk',20)
print(p1.__dict__)
p2=Person('lff',18)
a=[p1,p2]
# print(a)