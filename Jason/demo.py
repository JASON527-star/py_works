#print("哈哈哈")
# ...。。。英文状态 标点符号
#a=input("请输入密码：")
#print(a)
#print("我是水\n哈哈哈哈哈哈") \n 换行操作
#print("hello\tkkkk") #四个'空格' 补齐四个 \t 制表符
#print("hello    kkkk")
#print("hello\rpython") \r:覆盖
#print("hello\bpython") \b:删除 backspace
#print("\\")  两个\代表一个\
#print(r"你好\n我是急急急") # 使\后的失去作用
"""
import keyword
print(keyword.kwlist)

if 2>1:
    print("hhh") #缩进

a=2;b=3;c=4
ddd=a+b+c
print(ddd)
cc=[2,3,
    4,5
    ,34]
print(cc)
cd=(2,3,
    4,5
    ,34)
print(cd)

xxx="
名字：哈哈哈
年龄：1999
"
print(xxx)

abc="1566你好wadas" #字符串
bbb='sdasda哈哈哈哈哈'
"""
# //:向下取整      print(2**4):乘方

# a=None
# print(a+1)
# r=print(1234)
# print(r)
'''
字符串切片
'''
# name="小仙女长相甜美并且温柔" #切片[开始;结尾] 取左不取右
# print(name[-3:-1])
#print(name[0:6:2])
# print(name[::-1])  #字符串倒序输出
# kk='''
# qsdas
# hhhhhhhh
# '''
# print(kk)
'''
    字符串的拼接 用+
    拼接后加逗号用join
'''
# p='学习Python'
# q='我很快3333乐'
# s=','.join((p,q)) #拼接加逗号
# print(s)
'''
字符串的格式化
format()
'''
# print("大家好，我的名字是逍遥，今年18岁，性别男")
# s2="大家好，我的名字是{}，今年{}岁，性别{}".format("逍遥","18","男")
# s3="大家好，我的名字是{2}，今年{0}岁，性别{1}"
# print(s2)
# print(s3.format("逍遥","18","男"))

"""
字符串常用方法
find:查找元素位置 返回第一个出现的下标，找不到返回-1
count：统计字符串片段，在字符串中出现的次数
"""
# s1="pythonMuozhou"
# print(s1.count("o",6,12))

'''
字符串常用方法:
        replace:替换指定字符串片段 记得加引号
            参数3:替换的次数，从前往后替换
        upper:小写字母转大写
        lower:大写字母转小写
        title；每个单词首字母大写
        capitalize：第一个单词首字母大写
        swapcase：大小写互换
'''
# s1="python TO muzhonu"
# res1=s1.replace('on','TT',1)
# print(res1)
#
# res2=s1.capitalize()
# print(len(res2))
#
# res3=s1.lower()
# print(res3)

"""
    split:字符串分割 只能处理字符串类型数据
    参数1：分割点
    参数2：分割次数
    
    strip:去除字符串首尾的空格
"""
# s1="   111ab222ab333ab444    "
# #将字符串用规定字母a进行分割，得到列表
# s2=s1.split('a',2)
# print(s2)
# print(s1)
# print(s1.strip())
#
# s3='66656python:66657'
# print(s3.strip('6'))
#
# s4='      python:6666    muzhou:3434245'
# print(s4.replace(' ',''))

'''
传统格式化输出方法：%
    %s:字符串占位  可以放任何数据
    %d:数值类型占位
    %f：浮点数占位
    
'''
# s1='我%s你%s'%('爱','啊')
# print(s1)
# s2='1002%d3652'%(555.3)
# print(s2)
# s3='我的零花钱是%f'%(600)
# print(s3)
# name='陆博洋'
# age=18
# s4='我的名字是{}，年龄是{}'.format(name,age)
# s5=f'我的名字是{name}，年龄是{age}' #F也可以
# print(s4)
# print(s5)

'''
    len():字符串长度
    format:
    1：格式化小数长度(四舍五入)  :.2f
    2：百分比形式显示          :.3%
    数字(2和3)显示保留几位
'''

#s=3.6567
# x=5.6768
#print('今天的水果{:.2f}一斤'.format(s)) #冒号别忘了
# print('百分比为{1:.3%}'.format(0.3564,0.65891))

'''
列表

'''

# list1=[1,2,3,4,99,50,45,0]

# print(list1[5][2])
# print(len(list1[5]))
# list1[1]=5
# print(list1)

# list2=[1,2,3,4,88,50,45,89]
# # print(list1+list2)
# print(list1*8) #8个list1
# print('我按'*8)

'''
列表的切片取值
'''

# list_1=[10,20,30,40,50,60,70]
# print(list_1[::3])
# print(list_1[::-1])
# print(list_1[-6:-1:2])

'''
列表操作方法
    1:del关键字  删除
    2.append方法: 向列表末尾添加元素  extend
    3.insert :列表插入元素
'''
# a=[1,2,3]
#  del a[1] #在计算机内存中把a变量列表删除
#  a.extend([4,5,8]) #[1, 2, 3, 4, 5, 8]
#  a.append([4,5,8])  #[1, 2, 3, [4, 5, 8]]
# print(a)

# list_1=[10,20,40,50]
# list_1.insert(2,30)
# print(list_1)
# list_1.clear()
# print(list_1)
# print(len(list_1))

'''
    1.remove函数
    移除列表元素 有重复，只移除匹配的第一个
    2.pop函数    
        移除指定位置元素，返回要移除的元素

'''

# a=['hello','world','python','hello']
# b=['hello','world','python','hello']
#a.remove('hello')
#print(a)                  #['world', 'python', 'hello']
# b.pop(2) #只能填下标
# print(b)                    #['hello', 'world', 'hello']
# print('要移除的数据:',a.pop(2)) #要移除的数据: python
# print(a)                     #['hello', 'world', 'hello']

'''
    index函数 从列表中找出某个值第一个匹配项的索引位置
'''
# a=['hello','world','python','hello']
# r=a.index('hello',0,3)
# print(r) # 0
# a.reverse() #=print(a[::-1])
# print(a)

#a=[10,20,30]
#b=[10,20,30]
#a.extend([40,50]) #可以批量添加 与+的区别 用+占内存空间并返回新列表 而extend是在原列表追加
#b.append([40,50]) #append只能加一个
#print(a)          #[10, 20, 30, 40, 50]
#print(b)          #[10, 20, 30, [40, 50]]

'''
    copy函数
    用于创建列表副本
'''

# a=['hello','world','hello','python']
# b=a.copy()
# del a[1]
# print(b)  #['hello', 'world', 'hello', 'python']


# a=a=['hello','world','hello','python']
# b=a
# del a[1]
# print(b)  #['hello', 'hello', 'python']

'''
    sort函数：将列表进行排序(同类型)
    按Ascii码排序:0~9<A~Z<a~z
    count函数
'''
#a=['hello','world','kello','124python','哈哈哈哈哈']
#b=['hello','world','hello','124python','哈哈哈哈哈']
#a.sort()
# a.sort(reverse=True) #降序
#print(a)
#k=b.count('hello')
#print(k)

