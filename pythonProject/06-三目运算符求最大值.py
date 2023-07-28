'''
值1 if 条件判断 else 值2
如果条件判断成立,则返回值1;如果条件判断不成立,则返回else中的值2
案例:求两个数中的最大值
'''
num1 = 10
num2 = 100

# if num1 > num2 :
#     max = num1
# else:
#     max = num2

max = num1 if num1 > num2 else num2
print(max)