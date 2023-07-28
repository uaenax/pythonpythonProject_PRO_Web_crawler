class Fruit(object):
    def makejuice(self):
        pass


class Apple(Fruit):
    def makejuice(self):
        print('i can make apple juice!')


class Orange(Fruit):
    def makejuice(self):
        print('i can make orange juice!')


class Banana(Fruit):
    def makejuice(self):
        print('i can make banana juice!')


# 定义一个公共接口 => 多态特征 => 要求传入一个对象作为参数
def service(obj):
    obj.makejuice()


apple = Apple()
orange = Orange()
banana = Banana()
service(apple)
service(orange)
