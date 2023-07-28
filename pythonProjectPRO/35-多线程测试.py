import threading
import time


def music():
    for i in range(5):
        print('正在听音乐...')
        time.sleep(0.2)


def count():
    for i in range(5):
        print('正在写程序...')
        time.sleep(0.2)


if __name__ == '__main__':
    music_text = threading.Thread(target=music)
    count_text = threading.Thread(target=count)
    music_text.start()
    count_text.start()
