def decoration(flag):
    def logging(fn):
        def inner(*args, **kwargs):
            # 判断到底是加法还是减法运算
            if flag == '+':
                print(f'----正在做加法运算----')
            elif flag == '-':
                print(f'----正在做减法运算----')
            return fn(*args, **kwargs)

        return inner

    return logging


@decoration('+')
def sum_num(num1, num2):
    return num1 + num2


print(sum_num(10, 20))


@decoration('-')
def sud_num(num1, num2):
    return num1 - num2


print(sud_num(20, 10))
