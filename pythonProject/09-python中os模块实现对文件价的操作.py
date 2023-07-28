'''
案例: 准备一个static文件夹以及file1.txt、file2.txt、file3.txt三个文件
1.在程序中，将当前目录切换到static 文件来
2.创建一个新images 文件文返回到标签页
3.获取目下的所有文件
4.移除test文件夹
'''
import os

# 查看当前目录名称
os.getcwd()
# 切换目录
os.chdir('static')
print(os.getcwd())
# 创建images与text文件夹
if not os.path.exists('images'):
    os.mkdir('images')
if not os.path.exists('text'):
    os.mkdir('text')

# 获取一个目录下的所以文件
files = os.listdir()
print(files)
# 删除目录
if os.path.exists('text'):
    os.rmdir('text')