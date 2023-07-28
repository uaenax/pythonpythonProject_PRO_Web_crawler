'''
导入方法:
from 模块名称 import *                  代表导入这个模块中所有函数
from 模块名称 import 函数1,函数2,函数3    代表仅导入函数123

调用方式:不需要模块名称,直接使用函数名称即可
mkdir()
'''
# from os import *
from os import mkdir, rmdir

mkdir('static')
