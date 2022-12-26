phones=set()

for i in range(1,6):
    per=input('请输入第'+str(i)+'个朋友的姓名与手机号码:')
    phones.add(per)

for item in phones:
    print(item)