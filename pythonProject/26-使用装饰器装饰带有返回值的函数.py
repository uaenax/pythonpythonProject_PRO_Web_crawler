def logging(fn):
    def inner(a, b):
        print('---- 日志信息:正在进行计算------')
        return fn(a, b)

    return inner


@logging
def sum_num(num1, num2):
    sum = num1 + num2
    return sum


print(sum_num(10, 20))
