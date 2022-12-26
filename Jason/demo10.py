'''
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return '我的名字是{0},我今年{1}岁了'.format(self.name,self.age)
stu=student('张三',20)
print(stu)   #默认调用__str__这样的方法
print(type(stu))
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return '我的名字是{0},我今年{1}岁了'.format(self.name,self.age)
stu=student('张三',20)
print(stu)   #默认调用__str__这样的方法
print(type(stu))
'''



#多态

class Animal(object):
    def eat(self):
        print('动物会吃')
class Dog(Animal):
    def eat(self): #方法重写了
        print('狗吃骨头')
class Cat(Animal):
    def eat(self): #方法重写
        print('猫吃鱼')
class Person:
    def eat(self):
        print('人吃五谷杂粮')
def fun(obj):
    obj.eat()
fun(Dog())
fun(Cat())
fun(Animal())
print('----------')
fun(Person())



