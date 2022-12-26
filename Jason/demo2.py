#强制转换 int float

#a=123
#print(float(a))
#b='1234'
#print(float(b))
#c=3.56
#print(int(c))

#e='-3.256'
#print(int(e)) # 报错
#print(float(e))

'''
bool 强制转换
容器为空 ---->false  不空----->True

'''
# a=''
# b=[]
# c=()
# d={}
# e=set()
# print(bool(a),bool(b),bool(c),bool(d),bool(e))
# aa=12
# bb=0
# print(bool(aa),bool(bb))
'''
list() tuple、set类似
非容器类型 不能转换
字符串转列表，把每个字符当作列表元素
元组转列表，会把元组每个元素作为列表元素
字典转列表，只保留键
集合转列表，结果无序
'''
# d={'kk':'hh'}
# print(list(d))
# e={1,2,3,'a','哈哈哈哈'}
# print(list(e))

'''
dict
数字为非容器类型，不能转换
字符串不能转换（不能生成二级容器）
列表转字典 要为等长二级容器，且每个二级容器元素个数必须为2
元组转字典 要为等长二级容器，且每个二级容器元素个数必须为2
集合不能转换
'''

# a=1123
# b='aaa234嘎嘎嘎'
# c=[(1,2),('我','a')]
# #print(dict(c))
#
# d=([1,2],['我','a'])
# #print(dict(d))
# e={[1,2],['我','a']}
# print(dict(e))

'''
isinstance:断一个对象是否是一个已知的类型
isinstance(对象,对象类型)
返回布尔值,其中对象类型也可以是一个元组
'''
# a={'dddd'}
# print(isinstance(a,(int,float,str)))

'''
if...elif....else..
'''

# if 3>5:
#     print('你好')
# elif 4>7:
#     print('哈哈哈')
# else:
#     print('条件均不满足')

# a=int(input('请输入你的成绩:'))
# if a>3:
#     print('好')

'''
for 语句
1、遍历序列
不使用下标实现对序列每个元素的访问  列表/元组/字符串/字典/集合

'''
#for i in '1234568':
    #print(i)
#遍历数字 range()
# for k in range(1,5,2):
#     print(k)

#d={'name':'Jason','age':'15'}
# for a in d.items():
#     print(a)

# range() 函数步长

'''
双层for循环 if判断

'''
# a=[1,2,3,[10,20,30],[50,60,70]]
# b=[]
# k = 0
# for i in a:
#     if isinstance(i,list):
#         b.append(i)
# print(b)

'''
while 
可配合else使用
break  跳出for 和 while
continue 跳过当前循环块的剩余语句，进行下一轮循环
'''

# c=0
# while c<10:
#     print(c)
#     if c==4:
#         break
#     c+=1

# for i in 'python':
#     if i=='y':
#         continue
#     print('当前字母为:',i)

# a=0
# while a<6:
#     print('当前a的值为:', a)
#     a += 1
#     if a==4:
#         continue
        #break

# while a<6:
#     a += 1
#     if a==4:
#         continue
#     print('当前a的值为:', a)

'''
pass 空语句
pass语句又称为空语句或占位语句。
程序运行到pass语句时，什么也不做，直接跳过，运行后面的语句。
pass的作用就是为了保持程序结构的完整性
'''

# for letter in 'Python':
#    if letter == 'h':
#       pass
#       print ('这是 pass 块')
#    print('当前字母 :', letter)