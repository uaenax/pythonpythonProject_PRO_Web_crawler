# from multiprocessing import Process
# import time
#
#
# def task():
#     for i in range(4):
#         print(i)
#         time.sleep(1)
#
#
# if __name__ == '__main__':
#     p = Process(target=task)
#     p.start()
# from multiprocessing import Process
# import time
#
#
# # 定义在进程创建之前
# def task():
#     for i in range(4):
#         print(i)
#         time.sleep(1)
#
# if __name__ == '__main__':
#
#     p = Process(target=task)
#     p.start()
from multiprocessing import Process
import time

# def task(n):
#     for i in range(n):
#         print(i)
#         time.sleep(1)
#
#
# if __name__ == "__main__":
#     p = Process(target=task, args=(4,))
#     p.start()

# import threading
#
#
# # 定义线程执行函数
# def worker(data):
#     for d in data:
#         print(d)
#
#
# # 定义100个数据列表
# data_list = [i for i in range(100)]
#
# # 划分子列表，每个子列表包含20个数据
# sub_lists = [data_list[i:i + 20] for i in range(0, len(data_list), 20)]
#
# # 启动5个线程，分别传递子列表
# threads = []
# for sub_list in sub_lists:
#     t = threading.Thread(target=worker, args=(sub_list,))
#     threads.append(t)
#     t.start()

# # 等待所有线程执行完毕
# for t in threads:
#     t.join()

#
'''

实现如下需求：
1、开辟两个子进程
2、子进程1设置为死循环, 每隔1秒打印一次"进程信息"
3、子进程2接收一个整数类型参数, 进程2循环的次数即为传入的整形数字, 每隔1秒循环一次
4、当前的程序什么时候结束？
'''
# import multiprocessing
# import time
#
#
# def text1():
#     while True:
#         print("进程信息")
#         time.sleep(1)
#
#
# def text2(num):
#     for i in range(num):
#         print(f'第{i}次运行')
#         time.sleep(1)
#
#
# if __name__ == '__main__':
#     text1_pro = multiprocessing.Process(target=text1)
#     text2_pro = multiprocessing.Process(target=text2, args=(5,))
#     text1_pro.start()
#     text2_pro.start()
'''
实现如下需求：
创建一个子进程，以及一个全局变量。
子进程修改全局变量，然后每隔 1 秒打印全局变量的值和当前进程的 PID，
执行 10 次后退出；主进程等待子进程运行完成，最后打印出全局变量的值和当前进程的 PID。
'''
# import multiprocessing
# import time
# import os
# text_list = []
# def text():
#     for i in range(10):
#         text_list.append(i)
#         time.sleep(1)
#         print(text_list)
#         print(f'当前进程为{os.getpid()}')
#
# if __name__ == '__main__':
#     text_pro = multiprocessing.Process(target=text)
#     text_pro.start()
#     print(text_list)
#     print(os.getpid())
data_list = [i for i in range(100)]
list = [data_list[0:20]]
print(list)
