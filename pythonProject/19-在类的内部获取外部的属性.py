class Person(object):
    def infor_text(self):
        print(f'名字是{self.name}')
        print(f'年纪是{self.age}')
        print(f'手机号是{self.mon}')


p1 = Person()
p1.name = '张三'
p1.age = 18
p1.mon = 110

p1.infor_text()
