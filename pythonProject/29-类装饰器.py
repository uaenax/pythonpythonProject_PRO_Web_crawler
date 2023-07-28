class Check():
    def __init__(self, fn):
        self.__fn = fn

    def __call__(self, *args, **kwargs):
        # 添加额外添加的功能
        print('请先登录')
        # 调用comment函数本身 => __fn
        self.__fn()


@Check
def comment():
    print('发表评论')


comment()
