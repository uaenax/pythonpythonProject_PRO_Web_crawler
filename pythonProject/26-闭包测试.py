def outer():
    # 局部变量
    num2 = 100

    def inner():
        print(num2)

    return inner


# 全局变量 引用了 outer函数返回值
fn = outer()
fn()  # 找到inner函数在内存中的地址并立即执行print(num2) num2 = 100,所有弹出 100
