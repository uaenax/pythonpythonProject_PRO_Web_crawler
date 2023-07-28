class Student(object):
    def __init__(self, name, age, mobile):
        self.name = name
        self.age = age
        self.mobile = mobile

    def __str__(self):
        return f'学员姓名为:{self.name},年纪为:{self.age},电话为:{self.mobile}'



