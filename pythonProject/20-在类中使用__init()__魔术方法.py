class Person(object):
    def __init__(self, name, age, addren):
        self.name = name
        self.age = age
        self.addren = addren

    def __str__(self):
        return f'名称:{self.name},年纪:{self.age},住址:{self.addren}'

    def __del__(self):
        print('对象被清除')


p1 = Person('张三', 20, '中国')
print(p1.name)
print(p1.age)
print(p1.addren)
print(p1)
