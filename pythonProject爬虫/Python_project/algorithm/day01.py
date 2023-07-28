import time
# python排序算法
"""
# 1.冒泡排序
# 算法的主要时间消耗是比较的次数,执行交换的次数不确定,是一种效率很低的排序算法
# 冒泡排序共需要比较N-1轮,总共的比较次数为N(N-1)/2次
start_time = time.perf_counter()

# value = list((4, 2, 1, 5, 5, 3, 7, 6, 9, 8))
value = list((input("请输入:")))
for i in range(len(value)-1):
    flag = True
    for j in range(len(value)-1-i):
        if value[j] > value[j+1]:
            value[j],value[j+1] = value[j+1],value[j]
            flag = False
    if flag == True:
        break
print(value)

end_time = time.perf_counter()
print("代码运行时间为:{:.5}秒".format(end_time - start_time))
"""
# 2.选择排序
# 选择排序比冒泡排序执行效率高,选择排序共需要比较N-1轮,总共比较N(N-1)/2次
# 选择排序执行交换的次数是N-1
start_time1 = time.perf_counter()

value1 = list((3, 2, 4, 1, 7, 5, 5, 8, 6, 9))
for i in range(len(value1)-1):
    m = i
    for j in range(i+1,len(value1)):
        if value1[j] < value1[m]:
            m = j
    temp = value1[i]
    value1[i] = value1[m]
    value1[m] = temp
print(value1)

end_time1 = time.perf_counter()
print("代码运行时间为:{:.5}秒".format(end_time1 - start_time1))

# 递归函数
def average(n):
    s = 1
    for i in range(1,n+1):
        s *= i
    return s
c = average(5)
print (c)

def factorial(n):
    if n == 1:
        return 1
    else:
        s = n * factorial(n-1)
        return s
s = factorial(5)
print(s)







