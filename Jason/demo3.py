'''
创建函数
'''
#创建函数 def关键字
# def abc():
#     print('hhh')
# abc() #hhh
#括号用来传递参数

# def abc(a):
#     print(a)
# abc('hhh')

# def kk(a,b):
#     print(a+b)
# kk(100,200)
'''
默认参数
'''
# def kk(a=300,b=400):
#     print(a+b)
#kk()#700
#kk(600)#1000 默认赋给第一个
#kk(600,300)#900
# kk(b=1000)#1300

# def abc(a,b=[]):
#     b.append(a)
#     print(b)
# abc(100) #[100]
# abc(200) #[100, 200]
# abc(300) #[100, 200, 300]

# def abc(a,b=None):
#     if b is None:
#         b=[]
#     b.append(a)
#     print(b)
#
# abc(100) #[100]
# abc(200) #[200]
# abc(300) #[300]

'''
关键字参数
'''
# def abc(a=200,b=200):
#     print(a+b)
# abc(a=300,b=1000)#1300
'''
命名关键字参数
限定关键字形参
'''
# def abc(a,b=100,c=100): #默认参数后必须也是默认参数
#     print(a)
#     print(b)
#     print(c)
# abc(200,b=300,c=400)

# def abc(a,*,b,c): #*号之后也必须是关键字形参
#     print(a)
#     print(b)
#     print(c)
#abc(100,200,100) #报错
#abc(100,b=200,c=100)

'''
可变参数
*参数：最常见的变量名是args， 变量args指向一个tuple对象 元组
自动收集所有未匹配的位置参数到一个tuple对象，变量名args指向了此tuple对象
'''
# def abc(a,*args):
# def abc(a,*b): #或 def abc(a,*args):
#     print(a) #100
#     print(b) #() 空元组
#abc(100)
#100
#()
#abc(100,200)
#100
#(200,)
# abc(100,200,300,400,200)
#100
#(200, 300, 400, 200)

# def abc(a,**b):  #或 def abc(a,**kwargs): 字典
#     print(a)
#     print(b)

#abc(100,年龄='200')
#100
#{'年龄': '200'}

'''
参数的解包(拆包)：
      参数数据类型：字符串/列表/元组/集合/字典的时候可以解包
      传递实参时，可以在序列类型的参数前添加星号
      这样他会自动将序列中的元素一次作为参数传递
'''

# s='123'
# l=[1,2,3]
# k={1,2,3}
# kk=(1,2,3)
# p={
#     'a':'kk',
#     'b':'男',
#     'c':'python'
# }
# def abc(a,b,c):
#     print(a)
#     print(b)
#     print(c)
# abc(100,200,300)

# abc(*s) #解包
# abc(*k)
# abc(*l)
# abc(*kk)
# abc(*p) # 输出键值对的键
# abc(**p) #输出键值对的值 字典的键要对应
'''
参数解包和可变参数一起使用
**参数只收集未匹配的关键字参数
'''
# def abc(a,**kwargs):
#     print(a)
#     print(kwargs)
#
# abc(100,**{'x':100,'y':200})

'''
*args 需要在**kwargs之前

def abc(a,name='Jason',*args,**kwargs):
    print(a)
    print(name)
    print(args)
    for i in args:
        print(i)
    print(kwargs)
    for key,value in kwargs.items():
        print(key)
        print(value)

abc(100,'名字',1,2,4,2,x=100,y=300,z=233)

'''



'''
返回值
'''
# def kkk():
#     print(123)
#     return 9
# r=kkk()
# print(r)

#用return返回多个数据 返回元组

# def abc(a,b,c):
#     print('hhhh')
#     return a+10,b+34,c+34
# k=abc(100,2000,300)
# print(type(k))
# print(k)
#
# x,y,z= k #另外一种解包方法
# print(x)
# print(y)
# print(z)

'''
函数返回函数
    函数嵌套函数
    函数返回函数
'''
# def abc():
#     def xyz():
#         return [1,2,3]
#     return xyz
# k=abc() #k接收的是一个函数
# print(type(k)) #<class 'function'>
# print(k)       #<function abc.<locals>.xyz at 0x000002158A481820>
# r=k()
# print(r)       #[1, 2, 3]


# def make_car(made,size,**args):
#     print('制造商为：',made)
#     print('汽车型号：',size)
#     return args
# car=make_car('subzru','outback',color='blue',tow_package=True)
# print(car)

