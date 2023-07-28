def logging(fn):
    def inner(*args, **kwargs):
        print('-----日志信息------')
        return fn(*args, **kwargs)

    return inner

@logging
def sub_sum(num1, num2):
    return num1 - num2


print(sub_sum(20, 10))
