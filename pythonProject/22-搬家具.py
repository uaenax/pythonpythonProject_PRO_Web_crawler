'''
搬家具规则:
。1.家具分不同的类型，并占用不同的面积
。2.输出家具信息时，显示家具的类型和家具占用的面积
。3.房子有自己的地址和占用的面积
。4.房子可以添加家具，如果房子的剩余面积可以容纳家具，则提示家具添加成功;否则提示添加失败
。5.输出房子信息时，可以显示房子的地址、占地面积、剩余面积
'''


# 定义房子类
class Homes(object):
    def __init__(self, address, area):
        self.address = address
        self.area = area
        self.inte = []

    def __str__(self):
        strHome = f'住址是:{self.address},面积是{self.area},'
        if len(self.inte) > 0:
            for i in self.inte:
                strHome += f'{i},'
        strHome = strHome.strip(',')
        return strHome

    def add_infor(self, init):
        if init.getArea() < self.area:
            self.inte.append(init)
            self.area -= init.getArea()
            print(f'家具添加成功,房间剩余面积为{self.area}')
        else:
            print('房子剩余面积不足!,家具添加失败!')






# 定义家具类
class Bed(object):
    def __init__(self, name, area):
        self.__name = name
        self.__area = area

    def getName(self):
        return self.__name

    def getArea(self):
        return self.__area

    def __str__(self):
        return f'家具名称为:{self.__name},家具面积为:{self.__area}'


c1 = Bed('席梦思', 5)
c2 = Bed('人体工学椅',2)
h1 = Homes('北京昌平', 100)
h1.add_infor(c1)
h1.add_infor(c2)
print(h1)
