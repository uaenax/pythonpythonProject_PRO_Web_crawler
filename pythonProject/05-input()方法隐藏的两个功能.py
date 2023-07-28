'''
input() 方法,永远是str字符串类型
inp() 方法还具有一个"暂停"功能,阻塞后续代码的继续执行,直到用户输入完成以后,代码才可以继续向下执行
'''
# name = input('请输入你的名字:')
# print(f'你好,{name}')
# print(type(content))
# 定义三个变量
a = 1
b = 2
c = 3
# 打印变量以及变量数值
print(f'a={a},b={b},c={c}')
var1 = 8
var2 = 2.0
var3 = var1 / var2
print(var3)

var4 = var1 + var2 / var3
print(var4)
print("abc" >= "abd" and "itcast")
print(["a", "b", "c"] >= ["a", "b", "d"] or "itcast")

f = 7 % 3
print(f)