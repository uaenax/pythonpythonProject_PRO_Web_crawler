class Person(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def run(self):
        self.weight -= 0.1

    def eat(self):
        self.weight += 0.2

    def __str__(self):
        return f'姓名:{self.name},体重{self.weight:.2f}'


p1 = Person('小明', 80)
print(p1)

p1.eat()
print(p1)

p1.run()
print(p1)
