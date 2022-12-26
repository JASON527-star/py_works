'''
常用文件打开模式
'''
# file=open('b.txt','a')
# file.write('python')
# file.close()

'''
os模块
'''

#import os
# os.system('notepad.exe')
# os.system('calc.exe')
#直接调用可执行文件
# os.startfile('"C:\\Program Files (x86)\\Tencent\\TIM\\Bin\\QQScLauncher.exe"')

import matplotlib.pyplot as plt
squares = [1,4,9,16,25]
fig,ax=plt.subplots()
ax.plot(squares)
plt.show()
