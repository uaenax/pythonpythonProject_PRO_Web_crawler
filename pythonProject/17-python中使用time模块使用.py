'''
time模块是一个与时间相关的模块,主要拥有这样两个方法
time.sleep(秒数):休眠
time.time():获取当前时间,返回的是一个数字,我们经常使用time.time()获取程序执行时间
'''
import time
start = time.time()
list1 = []
for i in range(1000000):
    list1.append(i)
end = time.time()
print(f'以上程序执行一个消耗了{end - start}s时间')