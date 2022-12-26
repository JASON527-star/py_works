'''
字符串的编码与解码
'''

# s='伟大的中国梦'
# scode_gbk=s.encode('gbk')
# print(scode_gbk)
#
# scode_utf8=s.encode('utf-8')
# print(scode_utf8)
#
# #解码 bytes->str
# print(bytes.decode(scode_gbk,'gbk')) #伟大的中国梦
#
# print(bytes.decode(scode_utf8,'utf-8'))  #伟大的中国梦
#
# '''
# 数据的验证和处理
# '''
# s1='hello'
# s2='world'
# print('*'.join(['hello','world','python'])) #hello*world*python
# print(f'{s1}{s2}') #helloworld
# print('%s %s'%(s1,s2)) #hello world
# print('{0}{1}'.format(s1,s2)) #helloworld
#
# print('-------------------------------')
# #字符串去重
# s3='helloworldhhhsafaefoijdc'

# new_s3=''
# for item in s3:
#     if item not in new_s3:
#         new_s3+=item
# print(new_s3)
#      或者
# new_s3=''
# for i in range(len(s3)):
#     if s3[i] not in new_s3:
#         new_s3+=s3[i]
# print(new_s3) #helowrdsafijc
'''
*************
通过集合去重+ 列表的排序
*************
'''

# s4=set(s3)
# lst=list(s4)
# print(lst)
# lst.sort(key=s3.index)
# print(''.join(lst)) #helowrdsafijc

'''
列表元素去重
'''
#lst=['金星','水星','木星','火星','地球','土星','火星','天王星','金星','木星','地球','水星','冥王星']
# #(1)列表+not in
# new_lst1=[]
# for item in lst:
#     if item not in new_lst1:
#         new_lst1.append(item)
# print(new_lst1)
# #(2)
# new_lst2=[]
# for i in range(len(lst)):
#     if lst[i] not in new_lst2:
#         new_lst2.append(lst[i])
# print(new_lst2)
#
# #(3)
# new_lst3=set(lst)
# new_lst3=list(new_lst3)
# new_lst3.sort(key=lst.index)
# print(new_lst3)

'''
正则表达式
'''
# import re
# pattern=r'\d\.\d+'
# s='I study Python3.10 every day'
# match=re.match(pattern,s,re.I)
# print(match)
#
# s2='3.10Pyhon I study every day'
# match2=re.match(pattern,s2,re.I)
# print(match2)
# print('匹配的起始位置:',match2.start())
# print('匹配的结束位置:',match2.end())
# print('匹配区间的位置元组:',match2.span())
# print('匹配的字符串是:',match2.string)
# print('匹配的数据',match2.group())


# import re
# pattern='黑客|破解|反爬'
# s='我想学习Python,想破解一些VIP视频,Python可以实现无底线反爬吗'
# new_s=re.sub(pattern,'XXX',s)
# print(new_s)
#
# s2='http://www.baidu/s?wd=usj&ie=utf-8&tn=baidu'
# pattern2='[?|&]'
# lst=re.split(pattern2,s2)
# print(lst)

def fun(**kwpara):
    print(type(kwpara))
    for key,value in kwpara.items():
        print(key,'-------',value)
fun(**{'x':100,'y':200,'z':300})
#fun(x=100,y=200,z=300)
