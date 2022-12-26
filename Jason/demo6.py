'''
try:
    a=int(input('请输入第一个整数'))
    b=int(input('请输入第二个整数'))
    result=a/b
except BaseException as e:
    print('出错了',e)
else:
    print('计算结果为',result)
finally:
    print('无论是否异常，总会执行')
print('程序结束')
'''

'''
dic={2:{3:'sssss',4:'哈哈哈哈'},'asd':'rrrr'}
 for dic_value in dic.items():
     print(dic_value)
print(dic[2][4])
'''

'''
类的创建

'''

# class Student: #每个单词首字母大写,其余的小写
#     pass
# print(id(Student))   #内存空间
# print(type(Student))
# print(Student)

class Student:
    native_pace='吉林' #直接写在类里的变量, 称为类属性
    def eat(self):
        print('学生在吃饭') #定义在类里叫方法，定义在外边叫函数
    @staticmethod
    def method():
        print('我使用了staticmethod进行修饰，所以我是静态方法')
    @classmethod
    def method():
        print('我使用了classmethod进行修饰，所以我是类方法')

