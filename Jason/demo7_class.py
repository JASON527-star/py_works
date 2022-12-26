'''
class Student:
    native_pace='吉林' #直接写在类里的变量, 称为类属性
    def __init__(self,name,age): #实例属性
        self.name=name
        self.age=age
    def eat(self):
        print('学生在吃饭') #定义在类里叫方法，定义在外边叫函数
    @staticmethod
    def method():
        print('我使用了staticmethod进行修饰，所以我是静态方法')
    @classmethod
    def cm(cls):
        print('我使用了classmethod进行修饰，所以我是类方法')
'''


#创建Student类的对象

# stu1=Student('张三',20)
# print(id(stu1))
# print(type(stu1))
# print(stu1)
# stu1.eat()
# print(stu1.name)
# print(stu1.age)
# print('--------------------')
# Student.eat(stu1)

'''
stu1=Student('张三',20)
stu2=Student('李四',30)
print(stu1.native_pace)
print(stu2.native_pace)
Student.native_pace='天津'
print(stu1.native_pace)
print(stu2.native_pace)
print('------类方法的使用方式-------')
Student.cm()
print('-----静态方法使用方式-----')
Student.method()
'''
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print(self.name+'学生在吃饭')
stu1=Student('张三',20)
stu2=Student('李四',30)
print('----为stu2动态绑定性别属性------')
stu2.gender='男'
print(stu1.name,stu1.age)
print(stu2.name,stu2.age,stu2.gender)
print('--------------')
stu1.eat()
stu2.eat()

def show():
    print('定义在类之外的，称函数')
stu1.show=show
stu1.show()
stu2.show=show
stu2.show()