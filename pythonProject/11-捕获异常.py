num = int(input('请输入要进行除法运算的数字:'))
try:
    result = 10 / num
    print(result)
except:
    print('已经捕获异常,执行B方案!')
