#千年虫
lst=[88,89,90,98,00,99]
# 方法1
# for index in range(len(lst)):
#     if str(lst[index]) !='0':
#         lst[index]='19'+str(lst[index])
#     else:
#         lst[index] = '200' + str(lst[index])
# for index1 in range(len(lst)):
#     lst[index1]=int(lst[index1])
# print(lst)

#  方法2
# or 使用 enumerate函数

for index,value in enumerate(lst):
    if str(value) != '0':
        lst[index]='19'+str(lst[index])
    else:
        lst[index] = '200' + str(lst[index])
print(lst)
