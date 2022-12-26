'''
字符串处理方法

'''
# kk='kkkasdadwdas'
# kkk=kk.split('a')
# print(kkk)

s='HelloWorld'
print(s.center(39,'*'))  #字符串指定长度居中

ss='  Hello  World   '
print(ss.strip())  #去掉左右空格
print(ss.lstrip()) #去掉左空格
print(ss.rstrip()) #去掉右空格

s1='dl-HelloWorld'
print(s1.strip('ld')) #去除指定字符串,而且与顺序无关 -HelloWor
#但是中间的无法去除 如下:
s2='dl-HelloldWorld'
print(s2.strip('ld')) #-HelloldWor

'''
格式化字符串
'''
#使用占位符

name='马冬梅'
age=10
score=98.5
print('姓名:%s,年龄:%d,成绩:%f'%(name,age,score)) #姓名:马冬梅,年龄:10,成绩:98.500000

# f-string格式化字符串
print(f'姓名:{name},年龄:{age},成绩:{score}') #姓名:马冬梅,年龄:10,成绩:98.5

#str-format
print('姓名:{},年龄:{},成绩:{}'.format(name,age,score)) #姓名:马冬梅,年龄:10,成绩:98.5



'''
        format的格式控制
'''

ww='helloworld'
print('{0:*<20}'.format(ww)) #helloworld**********
print('{0:*>20}'.format(ww)) #**********helloworld
print('{0:*^20}'.format(ww)) #*****helloworld*****
print(ww.center(20,'*'))     #*****helloworld*****

#千位分隔符 只适用于整数和浮点数

print('{0:,}'.format(23482562482))        #23,482,562,482
print('{0:,}'.format(52368459637152.325)) #52,368,459,637,152.33

#浮点数小数部分精度
print('{0:.2f}'.format(3.152654))   #3.15

#字符串类型的最大显示长度
print('{0:.4}'.format('kaurfesf')) #kaur

#整数类型

a=425
print('{0:b},{0:c},{0:d},{0:x},{0:X}'.format(a)) #110101001,Ʃ,425,1a9,1A9
#b:二进制  c:对应Unicode字符  d:十进制  x:八进制   X:十六进制

b=3.1415926
print('{0:.2f},{0:.2E},{0:.2e},{0:.2%}'.format(b)) #3.14,3.14E+00,3.14e+00,314.16%


