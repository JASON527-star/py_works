'''

方法重写
'''
class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age,end='   ')

class Student(Person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)
        self.stu_no=stu_no
    def info(self):
        super().info()
        print(self.stu_no)

class Teacher(Person):
    def __init__(self,name,age,teacherfyear):
        super().__init__(name,age)
        self.teacherfyear=teacherfyear
    def info(self):
        super().info()
        print(self.teacherfyear)

stu=Student('张三',20,1001)
tea=Teacher('李四',30,123)

stu.info()
print('------------')
tea.info()
