dict_ticket={
    'G1569':['北京南-天津南','18:06','18:39','00:33'],
    'G1567':['北京南-天津南','18:15','18:49','00:34'],
    'G8917':['北京南-天津西','18:20','19:19','00:59'],
    'G203':['北京南-天津南','18:35','19:09','00:34'],
}
print(dict_ticket.keys())
print('车次   ''出发站-到达站   ''出发时间   ''到达时间   ''历时')

for key in dict_ticket.keys():
    print(key,end='  ')
    for item in dict_ticket.get(key):
        print(item,end='  ')
    print()

t=0
while True:
    flag=False
    train_num = input('请输入要购买的车次:')
    for num in dict_ticket.keys():
        if train_num != num :
            t+=1
        elif t==4:
            print('该车次不存在')
            break
        elif train_num == num:
            s1=dict_ticket.get(num)
            train_per=input('请输入乘车人,如果是多人请使用逗号分隔:')
            print('您已购买{}次列车,{} {}开,请{}尽快换取纸质车票.【铁路客服】'.format(num,s1[0],s1[1],train_per))
            flag=True
            break
    if flag==True:
        break

