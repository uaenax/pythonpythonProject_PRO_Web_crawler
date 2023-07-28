import time
import multiprocessing
import os


def working(t):
    print(f'获取当成子进程{os.getpid()}')
    print(f'主进程编号:{os.getppid()}')
    for i in range(3):
        print('working...')
        time.sleep(t)


if __name__ == '__main__':
    # 获取主进程的编号
    print(f'主进程编号:{os.getpid()}')

    # 创建一个子进程
    working_process = multiprocessing.Process(target=working, args=(0.2,))
    working_process.start()
