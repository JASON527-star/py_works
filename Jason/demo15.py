'''
常用内置模块

import sys
import time
import urllib.request
print(sys.getsizeof(24))
print(sys.getsizeof(45))
print(sys.getsizeof(True))
print(sys.getsizeof(False))
print(time.time())
print(time.localtime(time.time()))
print(urllib.request.urlopen('http://www.baidu.com').read())

'''

'''
外部模块导入
'''
import schedule
import time
def job():
    print('哈哈哈-----')

schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
