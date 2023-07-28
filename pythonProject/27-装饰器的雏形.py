'''
使用语法糖为循环计算程序运行所需时间
'''
import time


def get_time(fn):
    def inner():
        # 定义开始时间
        start = time.time()
        fn()
        # 定义结束时间
        end = time.time()
        print(f'此程序一个消耗了{end - start}s')

    return inner


@get_time
def dome():
    list1 = []
    for i in range(100000000):
        list1.append(i)


dome()
