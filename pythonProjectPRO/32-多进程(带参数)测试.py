import time
import multiprocessing


# n代表循环次数
def music(n):
    for i in range(n):
        print('听音乐')
        time.sleep(0.2)


# t代表停止时间
def coding(t):
    for i in range(5):
        print('写代码')
        time.sleep(t)


if __name__ == '__main__':
    music_pross = multiprocessing.Process(target=music, args=(5,))
    coding_pross = multiprocessing.Process(target=coding, kwargs={'t': 0.2})
    music_pross.start()
    coding_pross.start()
