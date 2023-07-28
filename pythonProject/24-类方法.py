class Tool(object):
    count = 0

    def __init__(self, name):
        self.name = name

        Tool.count += 1

    @classmethod
    def getCount(cls):
        return f'您一共实例了{cls.count}个对象'


p1 = Tool('小明')
p2 = Tool('小兰')
p3 = Tool('小绿')
print(Tool.getCount())
