'''
需求: 为其增加一个日志功能
'''


def logging(fn):
    def inner(a, b):
        print('---- 日志信息:正在进行计算------')
        fn(a, b)

    return inner


@logging
def sum_num(num1, num2):
    sum = num1 + num2
    print(sum)


sum_num(10, 20)
