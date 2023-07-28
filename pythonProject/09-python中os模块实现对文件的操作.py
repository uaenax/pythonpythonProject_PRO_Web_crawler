'''
os.rename(旧文件名称,新文件名称)
os.remove('要删除的文件名称')

案例:把python项目下的python.txt文件,更名为Linux.txt,并进行文件删除操作
'''
import os

if os.path.exists('python.txt'):
    os.rename('python.txt', 'linux.txt')

os.remove('linux.txt')
