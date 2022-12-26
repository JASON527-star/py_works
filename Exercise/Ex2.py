# lst=[]
# for i in range(5):
#     lst.append(input('请输入商品编号和商品名称进行商品入库，每次只能输入一件商品'))
# for index in range(5):
#     print(lst[index])
# # print(lst)
# k=[]
# for index1 in range(5):
#     k.append(input('请输入要购买的商品的编号'))
#     for index2 in range(5):
#         if k[index1] == lst[index2][0:4]:
#             print('商品已经添加到购物车，请继续添加要购买的商品编号:')
#         else:
#             print('该商品不存在！')
#             k[index1]=''
# print('您购物车里已经选择商品为:')
# for index3 in range(5):
#     for index4 in range(len(k)):
#         if lst[index3][0:4] == k[index4]:
#             print(lst[index3])



#    修改后


lst=[]
for i in range(5):
    lst.append(input('请输入商品编号和商品名称进行商品入库，每次只能输入一件商品'))
for index in range(5):
    print(lst[index])

k=[]
while True:
    item=input('请输入要购买的商品的编号')
    for index2 in range(5):
        if item == lst[index2][0:4]:
            print('商品已经添加到购物车，请继续添加要购买的商品编号:')
            k.append(lst[index2])
            break
        elif item != lst[index2][0:4] and index2==4:
            print('该商品不存在！')
            # k[index1]=''
    if item =='q':
        break

# print(k)
# print(lst)

print('您购物车里已经选择商品为:')
#lst.reverse()

k.reverse()
# print(lst1)
# print(len(lst1))
for kk in k:
    print(kk)
#print(lst1)


# 答案

# lst=[]
# for i in range(5):
#     goods=input('请输入商品编号和商品名称进行商品入库，每次只能输入一件商品:')
#     lst.append(goods)
# for item in lst:
#     print(item)
#
# cart=[]
# while True:
#     flag=False
#     num=input('请输入要购买的商品的编号:')
#     #遍历商品列表
#     for item in lst:
#         if num==item[0:4]:
#             flag=True
#             cart.append(item)
#             print('已添加到购物车')
#             break
#     if flag==False and num!='q':
#         print('该商品不存在!')
#     if num=='q':
#         break
#
# print('亲购物车的商品为：')
#
# cart.reverse()
# for item in cart:
#     print(item)

