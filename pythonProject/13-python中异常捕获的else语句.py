'''
完整的异常捕获语句:
try:
    可能出现异常的代码
excep Exception as e:
    如果出现异常,则执行的代码
else:
    如果try语句中的代码没有出现异常,则执行else中的代码
finally:
    特别适合实现一些收尾的工作,因为它是无论是否异常都会执行的代码 => f.close()
'''
try:
    f = open('python01.txt', 'r')
except:
    f = open('python01.txt', 'w')
else:
    cont = f.read()
    print(cont)
finally:
    f.close()
