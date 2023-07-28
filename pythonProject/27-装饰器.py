'''
需求:给comment发表评论函数增加一个额外的功能(要求先登录,有了账户以后才能发表评论),要求:不能改变现有comment的代码和调用方式
'''


def logging(fn):
    def inner():
        # 在引用fn函数之前,增加额外功能
        print('请先登录')
        # 引用局部变量fn
        fn()

    return inner


@logging
def comment():
    print('发表评论')


comment()
