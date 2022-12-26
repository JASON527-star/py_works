'''
面向对象特征：
封装 继承 多态

'''

'''
#封装

class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age  #
    def show(self):
        print(self.name,self.__age)

stu=Student('张三',20)
#在类的外部使用name和age
print(stu.name)
stu.show()
#print(stu.__age)  #会报错
'''

'''
print(stu.__age)

Traceback (most recent call last):
  File "D:\py_works\Jason\demo8.py", line 19, in <module>
    print(stu.__age)
AttributeError: 'Student' object has no attribute '__age'
'''
# stu.show()
# print(dir(stu))
# print(stu._Student__age)

#继承

class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)
        self.stu_no=stu_no

class Teacher(Person):
    def __init__(self,name,age,teacherfyear):
        super().__init__(name,age)
        self.teacherfyear=teacherfyear

stu=Student('张三',20,1001)
tea=Teacher('李四',30,123)

stu.info()
tea.info()

