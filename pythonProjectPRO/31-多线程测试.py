import time
import multiprocessing


def music():
    for i in range(5):
        print('听音乐')
        time.sleep(0.2)


def coding():
    for i in range(5):
        print('写代码')
        time.sleep(0.2)


if __name__ == '__main__':
    music_text = multiprocessing.Process(target=music)
    coding_text = multiprocessing.Process(target=coding)
    music_text.start()
    coding_text.start()
